from google import genai
from extractor import extract_text_from_pdf

# 1. Set up your API key
# WARNING: Keep this key secret! Do not share it or post it publicly.
API_KEY = "YOUR_API_KEY_HERE"  

# Initialize the new standard GenAI client
client = genai.Client(api_key=API_KEY)

def generate_tailored_resume(resume_text, job_description):
    # 2. Create the prompt instructions
    prompt = f"""
    You are an expert resume writer. 
    Compare the following Resume to the Job Description. 
    Briefly list the matching skills you found, and then list 3 critical missing skills the candidate should learn to prepare for an interview.
    
    RESUME TEXT: 
    {resume_text}
    
    JOB DESCRIPTION: 
    {job_description}
    """
    
    try:
        # 3. Send the prompt using the new standard method and the updated 2.5 model
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"An error occurred with the AI: {e}"

# Test the function
if __name__ == "__main__":
    print("1. Extracting resume text...")
    my_resume_text = extract_text_from_pdf("dummy_resume.pdf")
    
    dummy_jd = "We are looking for a Software Engineer with strong Python skills, experience in building APIs, and a solid understanding of SQL databases."
    
    print("2. Sending data to Gemini AI. This might take a few seconds...\n")
    ai_response = generate_tailored_resume(my_resume_text, dummy_jd)
    
    print("--- AI RESPONSE ---")
    print(ai_response)