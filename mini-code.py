def take_aptitude_test():
    score = 0
    
    questions = [
        {
            "question": "Which of the following activities do you enjoy the most?",
            "options": {
                "a": "Solving puzzles or logical problems",
                "b": "Creating art or expressing yourself creatively",
                "c": "Working with computers or technology",
                "d": "Helping and caring for others"
            }
        },
        {
            "question": "What type of working environment do you prefer?",
            "options": {
                "a": "A structured and organized setting",
                "b": "A flexible and dynamic environment",
                "c": "A collaborative team-based atmosphere",
                "d": "A peaceful and quiet workspace"
            }
        },
        {
            "question": "Which of the following values resonates with you the most?",
            "options": {
                "a": "Innovation and pushing boundaries",
                "b": "Freedom and independence",
                "c": "Collaboration and teamwork",
                "d": "Making a positive impact on others' lives"
            }
        },
        {
            "question": "Which of the following skills do you consider your strongest?",
            "options": {
                "a": "Analytical and problem-solving skills",
                "b": "Artistic or creative abilities",
                "c": "Technical or programming skills",
                "d": "Interpersonal and communication skills"
            }
        },
        {
            "question": "What are your long-term goals?",
            "options": {
                "a": "Becoming a leader or entrepreneur",
                "b": "Pursuing a career in the arts or entertainment",
                "c": "Advancing in the field of technology or engineering",
                "d": "Making a difference in people's lives or working in a helping profession"
            }
        },
        {
            "question": "How do you handle challenges or obstacles?",
            "options": {
                "a": "Analyzing the situation and finding practical solutions",
                "b": "Thinking creatively and finding unique approaches",
                "c": "Utilizing technical knowledge or tools to overcome difficulties",
                "d": "Seeking support from others and working collaboratively"
            }
        },
        {
            "question": "Which subject did you enjoy the most in school?",
            "options": {
                "a": "Mathematics or science",
                "b": "Fine arts or literature",
                "c": "Computer science or programming",
                "d": "Social sciences or psychology"
            }
        },
        {
            "question": "What type of tasks do you find yourself naturally gravitating towards?",
            "options": {
                "a": "Researching and analyzing data",
                "b": "Expressing ideas through visual or written mediums",
                "c": "Problem-solving and troubleshooting technical issues",
                "d": "Interacting and connecting with people"
            }
        },
        {
            "question": "What level of work-life balance are you seeking?",
            "options": {
                "a": "I'm willing to dedicate a significant amount of time to work",
                "b": "I prefer a balanced approach with time for personal interests",
                "c": "I enjoy a high level of flexibility and autonomy",
                "d": "I value a structured schedule and clear boundaries"
            }
        },
        {
            "question": "Which of the following industries interests you the most?",
            "options": {
                "a": "Finance or business",
                "b": "Media or entertainment",
                "c": "Technology or IT",
                "d": "Healthcare or social services"
            }
        },
        {
            "question": "What is your preferred method of learning and acquiring new skills?",
            "options": {
                "a": "Analyzing and studying information independently",
                "b": "Engaging in hands-on and experiential learning",
                "c": "Enrolling in technical courses or certifications",
                "d": "Collaborating and learning from others in a group setting"
            }
        },
        {
            "question": "Which of the following motivates you the most?",
            "options": {
                "a": "Solving complex problems and finding innovative solutions",
                "b": "Expressing creativity and originality in your work",
                "c": "Working with cutting-edge technology or tools",
                "d": "Making a positive impact on individuals or society as a whole"
            }
        },
        {
            "question": "How do you handle working under pressure or tight deadlines?",
            "options": {
                "a": "By organizing and prioritizing tasks effectively",
                "b": "By finding unique and creative solutions",
                "c": "By utilizing technical skills to streamline processes",
                "d": "By seeking support and assistance from others"
            }
        },
        {
            "question": "What level of financial stability are you looking for in your career?",
            "options": {
                "a": "It's important to me to have a high earning potential",
                "b": "I prioritize job satisfaction over financial gain",
                "c": "I value a balance between income and job fulfillment",
                "d": "I'm more focused on making a positive impact than financial rewards"
            }
        },
        {
            "question": "How important is continuous learning and professional growth to you?",
            "options": {
                "a": "It's essential for me to continuously learn and grow in my career",
                "b": "I enjoy learning, but it's not my top priority",
                "c": "I prefer to focus on gaining specialized technical knowledge",
                "d": "I value practical experience over continuous learning opportunities"
            }
        }
    ]
    
    for question in questions:
        print(question["question"])
        for option, value in question["options"].items():
            print(f"{option}) {value}")
        answer = input("Your answer (a, b, c, d, or s to skip): ")
        
        if answer.lower() == 's':
            print("You have chosen to skip this question.")
        elif answer.lower() in question["options"]:
            if answer.lower()=="a":
                score+=1
            if answer.lower()=="b":
                score+=2
            if answer.lower()=="c":
                score+=3
            if answer.lower()=="d":
                score+=4
   
    # Calculate the total score and suggest appropriate career options based on the score.
    print("\nCalculating your results...\n")
    print(score)
    if score >= 45:
        print("You are a Hrad worker with a heart wanting\n to learn and explore more,Here are\n some suggested jobs based on your mindset")
        career_options = ["Any Engineering field-","Software developer", "Data scientist", "Network engineer","Stack Developer","Law field","Medical field","Marketing Management"]
    elif score >= 30:
        print("You love working in stress but still\n want to explore a ittle more")
        career_options = ["Graphic designer", "Art director", "UX/UI designer",""]
    elif score >= 15:
        print("Based on you answers You are not sure what you want from lif \n you right now need a job to keep exploring whil earning\n")
        career_options = ["Media field", "Travel Guide", "Business consultant",""]
    elif score >= 3:
        print("you still haven't found anything which drives you\n but wish to do some low tress jobs. ")
        career_options = ["Librarian", "Nurse", "Social worker","Hairdresser"]
    else:
        career_options = []
    
    if career_options:
        print("Based on your answers, you may be suited for a career in the following fields:")
        print("Possible career options: " + ", ".join(career_options))
    else:
        print("Based on your answers, you may benefit from exploring a wide range of career options to discover your strengths and interests.")
    
    # Customize career suggestions and further steps based on the chosen career field or area of interest.
    chosen_field = input("\nEnter your desired career field or area of interest: ")
    if chosen_field:
        print(f"\nHere are some personalized career suggestions for the {chosen_field} field:")
        # Provide customized career suggestions based on the user's chosen field and the score.
        # Feel free to customize this section to fit your criteria.
        if chosen_field.lower() == "technology" or chosen_field.lower() == "it":
            print("Based on your interests and skills, you may consider the following career options in the technology or IT field:")
            print("- Software engineer/developer: Building and maintaining software applications.")
            print("- Data analyst/scientist: Analyzing and interpreting complex data.")
            print("- Cybersecurity specialist: Protecting computer systems and networks from security threats.")
            print("- IT project manager: Overseeing and coordinating technology projects.")
        elif chosen_field.lower() == "business" or chosen_field.lower() == "finance":
            print("Based on your interests and skills, you may consider the following career options in the business or finance field:")
            print("- Financial analyst: Analyzing financial data and providing investment recommendations.")
            print("- Marketing manager: Developing and implementing marketing strategies.")
            print("- Business consultant: Advising companies on improving their operations and performance.")
            print("- Entrepreneur: Starting and managing your own business venture.")
        elif chosen_field.lower() == "art" or chosen_field.lower() == "media":
            print("Based on your interests and skills, you may consider the following career options in the art or media field:")
            print("- Graphic designer: Creating visual concepts and designs.")
            print("- Art director: Managing and coordinating artistic projects.")
            print("- Film director: Directing and overseeing the production of films or videos.")
            print("- Social media manager: Developing and implementing social media strategies.")
        elif chosen_field.lower() == "healthcare" or chosen_field.lower() == "social services":
            print("Based on your interests and skills, you may consider the following career options in the healthcare or social services field:")
            print("- Doctor: Diagnosing and treating medical conditions.")
            print("- Nurse: Providing patient care and assisting in medical procedures.")
            print("- Social worker: Helping individuals and communities navigate social challenges.")
            print("- Occupational therapist: Assisting people in recovering and developing necessary skills for daily living.")
        else:
            print("Unfortunately, we don't have specific career suggestions for the chosen field. However, you can explore related fields and job roles based on your interests and skills.")
    
        # Provide further steps tailored to the chosen career field.
        print("\nTo explore these options further, you can:")
        print("- Research specific job roles and responsibilities in your chosen field.")
        print("- Speak with professionals who work in the field to gain insights and advice.")
        print("- Consider pursuing relevant education or certifications to enhance your knowledge and skills.")
        print("- Seek internships or entry-level positions to gain practical experience.")
    else:
        print("\nTo explore these options further, you can research specific job roles, speak with professionals in those fields, and consider seeking career counseling for personalized guidance.")
    
    # Ask the user if they want to retake the test
    retake = input("\nWould you like to retake the test? (yes/no): ")
    if retake.lower() == "yes":
        print("\nLet's retake the test!")
        take_aptitude_test()
    else:
        print("\nThank you for taking the aptitude test!")

# Call the function to start the aptitude test
take_aptitude_test()