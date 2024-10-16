import pandas as pd
import os 

# Data for the CSV file
faq_data = {
    "Question": [
        "What courses does Upflairs offer?",
        "How can I enroll in a course?",
        "Are there any prerequisites for enrolling in the courses?",
        "Do you offer internships after the course completion?",
        "How long is the internship program at Upflairs?",
        "Will I get a certificate after completing the internship?",
        "Is the internship paid or unpaid?",
        "Does Upflairs provide a job placement after course completion?",
        "Can I access recorded lectures if I miss a live class?",
        "Is there any career guidance or support at Upflairs?",
        "Are the courses at Upflairs self-paced?",
        "What are the payment options for Upflairs courses?",
        "Is there any refund policy at Upflairs?",
        "How do I contact support if I have any questions?"
    ],
    "Answer": [
        "Upflairs offers courses in Data Science and Machine Learning, DevOps, Full Stack Development, IoT, and System Embedding. We also provide internships to help you gain real-world experience.",
        "You can enroll in any course by visiting the Upflairs website, selecting the course you're interested in, and clicking the 'Enroll Now' button. You'll be prompted to complete your registration and payment.",
        "Most courses at Upflairs do not require specific prerequisites. However, some technical courses like Full Stack Development or DevOps may benefit from prior knowledge of programming or cloud computing.",
        "Yes! Upflairs offers internship opportunities for students who successfully complete our courses, allowing you to gain practical industry experience.",
        "Our internship programs typically last 3-6 months, depending on the field and project complexity. You'll get hands-on experience and work with industry professionals.",
        "Yes, upon successfully completing the internship, you will receive a certificate of completion that you can showcase in your portfolio or resume.",
        "Upflairs offers both paid and unpaid internship opportunities. Specific details are provided based on the project and your role.",
        "While Upflairs does not guarantee job placements, we offer career counseling, resume-building workshops, and interview preparation to help you secure a job in your desired field.",
        "Yes, all our live classes are recorded, and you can access them at any time from your student portal.",
        "Yes, we offer career counseling, resume-building workshops, and interview preparation sessions to help students advance in their careers.",
        "Some courses are self-paced, while others have live sessions. Details for each course are provided on our course page.",
        "We accept various payment options including credit/debit cards, net banking, and UPI. Flexible EMI options are also available for some courses.",
        "Yes, we have a refund policy in place. You can request a refund within the first 7 days of course enrollment if you're unsatisfied.",
        "You can contact our support team by emailing support@upflairs.com or through the live chat feature on our website."
    ]
}

# Creating DataFrame
faq_df = pd.DataFrame(faq_data)

data_folder_path = r"D:\Achievements\freelancing\GenerativeAI\Domain_specific_with_RAG\Data"
file_name = "upflairs_question_answer.csv"
upflairs_data_file_path = os.path.join(data_folder_path,file_name)
# Saving to CSV
faq_df.to_csv(upflairs_data_file_path, index=False)
print("Successfully written your data into folder : ",upflairs_data_file_path)
