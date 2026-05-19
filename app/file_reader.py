from pypdf import PdfReader


def read_resume_file(file):

    file_extension = file.filename.split(".")[-1].lower()

    try:

        if file_extension == "txt":

            content = file.file.read()

            return content.decode("utf-8")

        elif file_extension == "pdf":

            pdf = PdfReader(file.file)

            text = ""

            for page in pdf.pages:

                extracted_text = page.extract_text()

                if extracted_text:
                    text += extracted_text

            return text

        return None

    except Exception as error:

        print("File Reading Error:", error)

        return None