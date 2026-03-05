import requests

API_BASE = "http://localhost:8000"
HEALTH_URL = f"{API_BASE}/health"
ASK_URL = f"{API_BASE}/ask"

def check_health():
    try:
        response = requests.get(HEALTH_URL)
        if response.status_code == 200:
            print("API is healthy.")
            return True
        else:
            print(f"API returned status: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("Could not connect to API. Is the server running?")
        return False


def test_ask_endpoint():

    while True:
        try:
            question = input("Enter your question: ").strip()

        except KeyboardInterrupt:
            print("\n Exiting.")
            break
        
        if question.lower() in ["exit", "quit"]:
            print(" Exiting.")
            break

        payload = {"query": question}
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(ASK_URL, json=payload, headers=headers)
            response.raise_for_status()

            data = response.json()

            print(f"Answer: {data.get('answer')}")
            print(f"Source Document: {data.get('source')}")
        
        except Exception as e:
            print(e)
            if response.text:
                print(f"Error details: {response.text}")

if __name__ == "__main__":
    if check_health():
        test_ask_endpoint()