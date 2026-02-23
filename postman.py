import tkinter as tk
import requests

def send_request():
    url = url_entry.get()
    method = method_var.get()
    try:
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url)
        elif method == "PUT":
            response = requests.put(url)
        elif method == "DELETE":
            response = requests.delete(url)
        else:
            response = None
        
        if response:
            response_text.delete(1.0, tk.END)
            response_text.insert(tk.END, f"Status: {response.status_code}\n\n{response.text}")
        
    except Exception as e:
        response_text.delete(1.0, tk.END)
        response_text.insert(tk.END, f"Error: {str(e)}")

#GUI
root = tk.Tk()
root.title("Mini Postman")

tk.Label(root, text="URL:").pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

tk.Label(root, text="Método:").pack()
method_var = tk.StringVar(value="GET")
method_menu = tk.OptionMenu(root, method_var, "GET", "POST", "PUT", "DELETE")
method_menu.pack()

tk.Label(root, text="Body (para POST/PUT):").pack()
body_text = tk.Text(root, height=5, width=50)
body_text.pack()

send_button = tk.Button(root, text="Enviar", command=send_request)
send_button.pack()

tk.Label(root, text="Resposta:").pack()
response_text = tk.Text(root, height=15, width=70)
response_text.pack()

root.mainloop()
        
