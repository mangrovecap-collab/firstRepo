# Clinical Notes Logger
# Prompts for patient ID and clinical note, then appends to clinicalNotes.txt

# Get patient ID from user
patient_id = input("Enter Patient ID: ")

# Get clinical note from user
clinical_note = input("Enter Clinical Note: ")

# Open file in append mode ('a') - creates file if it doesn't exist
with open('clinicalNotes.txt', 'a') as file:
    # Write patient ID and note with timestamp and separator
    file.write(f"\n{'='*50}\n")
    file.write(f"Patient ID: {patient_id}\n")
    file.write(f"Date/Time: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write(f"Clinical Note: {clinical_note}\n")
    file.write(f"{'='*50}\n")

print("Clinical note has been saved to clinicalNotes.txt")
