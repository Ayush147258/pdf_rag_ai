from src.rag import (
    index_pdf,
    index_all_pdfs,
    ask_question,
    reset_history,
    list_pdfs,
    clear_index,
)
def main():

    while True:

        print("1. Index PDF")
        print("2. Index ALL PDFs")
        print("3. Ask Question")
        print("4. Reset Chat")
        print("5. Show PDFs")
        print("6. Clear Index")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            file_name = input("Enter PDF name (inside data/pdfs): ")
            index_pdf(file_name)
            print("PDF indexed!")

        elif choice == "2":

            print(index_all_pdfs())

        elif choice == "3":

            question = input("Ask: ")
            answer = ask_question(question)
            print("\nAnswer:\n")
            print(answer)

        elif choice == "4":

            print(reset_history())

        elif choice == "5":

            print(list_pdfs())

        elif choice == "6":
            print(clear_index())

        elif choice == "7":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()