 # Prompt 1: Activities
    activity_prompt = f"Suggest 5 employee engagement activities for celebrating {festival} in a company."

    activities = generate_response(
        activity_prompt,
        temperature,
        top_p,
        max_tokens
    )

    # Prompt 2: Email
    email_prompt = f"Write a professional email announcement for celebrating {festival} in the workplace."

    email = generate_response(
        email_prompt,
        temperature,
        top_p,
        max_tokens
    )

    return activities, email

# Gradio Input elements
import gradio as gr
festival_input = gr.Textbox(label="Festival Name")
temperature_input = gr.Slider(0.0, 1.0, label="Temperature")
top_p_input = gr.Slider(0.0, 1.0, label="Top-P")
max_tokens_input = gr.Number(label="Max Tokens")

# Gradio Output elements
activities_output = gr.Textbox(label="Employee Engagement Activities")
email_output = gr.Textbox(label="Email Announcement")


# Gradio Interface
interface = gr.Interface(
    fn=process_festival,
    inputs=[festival_input, temperature_input, top_p_input, max_tokens_input],
    outputs=[activities_output, email_output],
    title="Festival Engagement Generator",
    description="Generate employee activities and email announcements for any festival."
)

# Launch Interface
interface.launch()
