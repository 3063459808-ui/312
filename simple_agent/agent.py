import os

# Get the directory where the script is located to build a reliable path
script_dir = os.path.dirname(os.path.abspath(__file__))
KNOWLEDGE_FILE_PATH = os.path.join(script_dir, "knowledge.txt")

def read_knowledge_base(filepath):
    """Reads the knowledge base file and returns a list of sentences."""
    if not os.path.exists(filepath):
        return []
    with open(filepath, 'r', encoding='utf-8') as f:
        # Read lines and strip any leading/trailing whitespace, ignore empty lines
        lines = [line.strip() for line in f.readlines() if line.strip()]
    return lines

def find_answer(question, knowledge_base):
    """
    Finds an answer by matching non-stopword keywords from the question.
    """
    # First, handle empty or whitespace-only input
    if not question.strip():
        return "请输入一个问题。"

    stop_words = {'a', 'an', 'the', 'is', 'are', 'what', 'of', 'in', 'is', 'are', 'was', 'were', 'who', 'where', 'when', 'why', 'how', 'on', 'at', 'for'}

    # Sanitize and get keywords from the question, filtering out stop words
    question_words = set(question.lower().strip().replace('?', '').split())
    keywords = question_words - stop_words

    # If the question contained only stop words, we can't find a specific answer.
    if not keywords:
        return "请在您的问题中提供更具体的关键词。"

    found_answers = []
    for sentence in knowledge_base:
        sentence_words = set(sentence.lower().replace('.', '').split())
        # Check for intersection between keywords and sentence words
        if not keywords.isdisjoint(sentence_words):
            found_answers.append(sentence)

    if not found_answers:
        return "抱歉，我不知道这个问题的答案。"

    return "\n".join(found_answers)

def main():
    """
    Main function to run the agent's command-line interface.
    """
    knowledge_base = read_knowledge_base(KNOWLEDGE_FILE_PATH)

    if not knowledge_base:
        print(f"错误: 知识库文件 '{KNOWLEDGE_FILE_PATH}' 未找到或为空。代理无法启动。")
        return

    print("你好！我是一个简单的事实问答代理。")
    print("你可以问我关于知识库里的问题。输入 'exit' 或 'quit' 退出。")

    while True:
        try:
            question = input("你问: ")
            if question.lower() in ["exit", "quit"]:
                print("代理: 再见！")
                break

            answer = find_answer(question, knowledge_base)
            print(f"代理: {answer}")
        except (EOFError, KeyboardInterrupt):
            print("\n代理: 再见！")
            break

if __name__ == "__main__":
    main()
