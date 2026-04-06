# skills.md — UC-X Document QA
# Path: uc-x/skills.md

skills:

  - name: load_documents
    description: Load all policy documents into memory.
    input: >
      directory_path (string)
    output: >
      dict {filename: text}
    error_handling: >
      Skip unreadable files, raise error if directory missing.

  - name: find_relevant_document
    description: Identify the most relevant document for a question.
    input: >
      question (string), documents (dict)
    output: >
      selected_document_text (string)
    error_handling: >
      If no relevant document found → return None.

  - name: extract_answer
    description: Extract answer from selected document.
    input: >
      question (string), document_text (string)
    output: >
      answer (string)
    error_handling: >
      If answer not found → return 'INSUFFICIENT_INFORMATION'.

  - name: return_response
    description: Return final answer.
    input: >
      answer (string)
    output: >
      string
    error_handling: >
      Ensure no extra text or formatting.