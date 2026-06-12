import os
from dotenv import load_dotenv
from src.crew import UjimaAgentPride

load_dotenv()

def run_prototype_demo():
    print("="*60)
    print("UJIMA FINTECH AGENT PRIDE PROTOTYPE WORKFLOW ENGINE")
    print("="*60)

    # Simulated Red Team Input Vector
    # 38yo female trader in Busia with 4 children requesting KES 28,000 for school fees
    mock_input_payload = {
        "name": "Grace Omondi",
        "age": 38,
        "occupation": "Maize Vendor / Informal Trader",
        "location": "Busia County",
        "dependents": 4,
        "requested_amount": 28000,
        "user_message": "My cash reserves are currently low because of the planting season, but I need money for my children's school fees before the next major harvest cycle."
    }

    print(f"[*] Processing Incoming Request via Ujima Ecosystem...")
    print(f"[-] Profile: {mock_input_payload['name']} | Amount: KES {mock_input_payload['requested_amount']}")
    
    # Initialize Core System
    pride_engine = UjimaAgentPride()
    final_briefing = pride_engine.assemble_pride(mock_input_payload)

    print("\n" + "="*50)
    print("FINAL HUMAN OFFICER BRIEFING RECEIVED (GUARD COMPLIANT):")
    print("="*50)
    print(final_briefing)

if __name__ == "__main__":
    run_prototype_demo()