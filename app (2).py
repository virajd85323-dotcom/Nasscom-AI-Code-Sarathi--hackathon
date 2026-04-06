# Path: uc-x/app.py

import os
import argparse
import re


# -------------------------------
# Load documents
# -------------------------------
def load_documents(folder_path):
    docs = {}
    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
                docs[file] = f.read()
    return docs


# -------------------------------
# Select document (NO MIXING)
# -------------------------------
def find_relevant_document(question, documents):
    question = question.lower()

    if "leave" in question:
        return documents.get("policy_hr_leave.txt"), "policy_hr_leave.txt"

    if "reimbursement" in question or "expense" in question:
        return documents.get("policy_finance_reimbursement.txt"), "policy_finance_reimbursement.txt"

    if "internet" in question or "usage" in question or "access" in question:
        return documents.get("policy_it_acceptable_use.txt"), "policy_it_acceptable_use.txt"

    return None, None


# -------------------------------
# Extract best answer (FINAL LOGIC)
# -------------------------------
def extract_answer(question, doc):
    if doc is None:
        return None

    question = question.lower()

    # 🚫 Trap: file-related questions → refuse
    if "file" in question or "files" in question:
        return None

    sentences = re.split(r'\.\s+', doc)

    best_sentence = ""
    max_score = 0

    for s in sentences:
        s_clean = s.strip()

        # ❌ Skip headers / noise
        if not s_clean:
            continue
        if s_clean.isupper():
            continue
        if "policy" in s_clean.lower() and "section" not in s_clean.lower():
            continue
        if len(s_clean.split()) < 6:
            continue

        # ✅ Score relevance
        score = sum(
            1 for word in question.split()
            if len(word) > 4 and word in s_clean.lower()
        )

        if score > max_score:
            max_score = score
            best_sentence = s_clean

    if max_score == 0:
        return None

    return best_sentence


# -------------------------------
# Refusal template
# -------------------------------
def refusal():
    return (
        "This question is not covered in the available policy documents "
        "(policy_hr_leave.txt, policy_it_acceptable_use.txt, policy_finance_reimbursement.txt). "
        "Please contact the relevant team for guidance."
    )


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--question", required=True)
    parser.add_argument("--docs", required=True)

    args = parser.parse_args()

    try:
        documents = load_documents(args.docs)

        doc, doc_name = find_relevant_document(args.question, documents)

        answer = extract_answer(args.question, doc)

        if doc_name is None or answer is None:
            print(refusal())
        else:
            print(f"Source: {doc_name}")
            print(f"Answer: {answer}")

    except Exception as e:
        print("❌ Error:", str(e))