import tkinter as tk
from tkinter import filedialog
import cv2
import pytesseract
import pandas as pd

root = tk.Tk()
root.title("Number Plate Recognition")

def open_image():
        file_path = filedialog.askopenfilename()
        # Load the image
        image = cv2.imread("/home/cherry/Documents/myFolder/plate1.jpeg")

        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Perform OCR on the detected region
        ocr_result = pytesseract.image_to_string(gray)
       
        # Display the OCR result on the GUI
        ocr_label.config(text=f"OCR Result: {ocr_result}")

def open_excel_file():
    excel_file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    if excel_file_path:
        # Read the Excel data using pandas
        excel_data = pd.read_excel('/home/cherry/Documents/myFolder/BUS_INFO.xlsx')
       
        number_plate_column = 'Bus_Number'
        detected_plate = 'ocr_result'  # Replace with the actual detected plate

    # Check if the detected plate exists in the Excel data
    if detected_plate in excel_data[number_plate_column].values:
        # If it's a match, you can retrieve other data associated with the plate
        matched_data = excel_data[excel_data[number_plate_column] == detected_plate]
        print("Matched Data:")
        print(matched_data)
    else:
        print("No match found for detected plate.")

        # Extract relevant data based on the detected number plate
        detected_plate = detected_label.cget("text").split(": ")[-1]
        matched_data = excel_data.loc[excel_data['Bus_Number'] == detected_plate]
       
        # Display the matched data on the GUI
        data_label.config(text=f"Matched Data: {matched_data.to_string(index=False)}")

# Create a button to open an image
image_button = tk.Button(root, text="Open Image", command=open_image)
image_button.pack()

# Create a button to open an Excel file
excel_button = tk.Button(root, text="Open Excel File", command=open_excel_file)
excel_button.pack()

# Create labels to display the detected plate, OCR result, and matched data
detected_label = tk.Label(root, text="")
detected_label.pack()
ocr_label = tk.Label(root, text="")
ocr_label.pack()
data_label = tk.Label(root, text="")
data_label.pack()

# Start the Tkinter main loop
root.mainloop()
cv2.waitKey(0)
cv2.destroyAllWindows()

