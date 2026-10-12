"""Automated verification test for AgentArmy Gemini Framework."""
import os
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO_ROOT)

from framework.doctrine_retriever import DoctrineRetriever
from framework.location_manager import LocationManager
from framework.gemini_factory import GeminiFactory


def test_retriever():
    r = DoctrineRetriever()
    assert len(r.catalog) > 100, "Catalog should have > 100 documents"
    assert len(r.messages) > 100, "Messages catalog should have > 100 messages"

    # Test extracting AR 601-210 para 2-3 (Age)
    para = r.extract_paragraph_text("AR_601-210", "2-3")
    assert para is not None, "Failed extracting AR 601-210 2-3"
    assert "Age" in para["title"]
    assert "Applicant is eligible for enlistment" in para["text"]
    print("[PASS] DoctrineRetriever passed")


def test_location_manager():
    lm = LocationManager()
    assert len(lm.overlays) >= 2, "Should have loaded location overlays"

    detected = lm.detect_locations("Processing at Charlotte MEPS")
    assert any(d["id"] == "charlotte_meps" for d in detected), "Should detect Charlotte MEPS"

    overlays = lm.get_overlays_for_agent("07_medical_standards", "Charlotte MEPS")
    assert len(overlays) >= 1, "Should find overlay for 07_medical_standards"
    assert "Charlotte MEPS" in overlays[0]["title"]
    print("[PASS] LocationManager passed")


def test_factory_and_routing():
    factory = GeminiFactory()
    assert len(factory.specialists) == 43, f"Expected 43 specialists, got {len(factory.specialists)}"
    assert factory.orchestrator is not None, "Orchestrator must be initialized"

    # Test 1: NPS basic eligibility
    res1 = factory.ask("What is the enlistment age limit for an applicant without prior service?")
    assert res1["routed_agent"]["id"] == "01_basic_eligibility", f"Wrong route: {res1['routed_agent']['id']}"

    # Test 2: Prior Service
    res2 = factory.ask("Can a veteran with prior service enlist with an RE-3 code?")
    assert res2["routed_agent"]["id"] == "13_prior_service", f"Wrong route: {res2['routed_agent']['id']}"

    # Test 3: Location injection into medical standards
    res3 = factory.ask("What are the prescreen cutoff times?", location_context="Charlotte MEPS")
    assert res3["routed_agent"]["id"] == "07_medical_standards", f"Wrong route: {res3['routed_agent']['id']}"
    assert "Charlotte MEPS" in res3["answer"] or "Prescreen" in res3["answer"]

    # Test 4: Education credentialing (Tier 1 vs Tier 2, GED, college credits)
    res4 = factory.ask("Can an applicant with a GED and 15 college credits qualify as Tier 1?")
    assert res4["routed_agent"]["id"] == "03_education_credentialing", f"Wrong route: {res4['routed_agent']['id']}"

    # Test 5: Enlistment incentives / bonuses
    res5 = factory.ask("What enlistment bonus and student loan repayment incentives are available?")
    assert res5["routed_agent"]["id"] in ("19_ra_options_incentives", "20_srip"), f"Wrong route: {res5['routed_agent']['id']}"

    print("[PASS] GeminiFactory routing passed")


if __name__ == "__main__":
    test_retriever()
    test_location_manager()
    test_factory_and_routing()
    print("\nALL VERIFICATION TESTS PASSED SUCCESSFULLY!")
