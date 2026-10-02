import tkinter as tk
from tkinter import ttk, messagebox

# ============================================================
# MOBILE PHONE TROUBLESHOOTING EXPERT SYSTEM
# Python + Tkinter
# 20 IF-THEN Rules
# ============================================================


# ============================================================
# KNOWLEDGE BASE - 20 RULES
# ============================================================

rules = {
    "Battery draining fast": {
        "cause": "Background apps are running or battery usage is high.",
        "solution": "Close unnecessary background apps and reduce battery usage."
    },

    "Phone overheating": {
        "cause": "Heavy applications or continuous phone usage.",
        "solution": "Close heavy applications and allow the phone to cool."
    },

    "Network not working": {
        "cause": "Weak network signal or Airplane mode is enabled.",
        "solution": "Check Airplane mode and move to an area with better signal."
    },

    "Wi-Fi not connecting": {
        "cause": "Wi-Fi connection or router problem.",
        "solution": "Reconnect to Wi-Fi or restart the router."
    },

    "Storage full": {
        "cause": "Too many files, photos, videos, or applications.",
        "solution": "Delete unnecessary files and uninstall unused applications."
    },

    "Phone is slow": {
        "cause": "Low storage or too many background applications.",
        "solution": "Free storage space and close unnecessary applications."
    },

    "Apps crashing": {
        "cause": "Application may be outdated or corrupted.",
        "solution": "Update the application or reinstall it."
    },

    "Phone not charging": {
        "cause": "Charger, charging cable, or charging port problem.",
        "solution": "Check the charger and cable. Try another compatible charger."
    },

    "No sound": {
        "cause": "Silent mode is enabled or volume is low.",
        "solution": "Turn off silent mode and increase the volume."
    },

    "Screen freezing": {
        "cause": "Application or system software issue.",
        "solution": "Restart the phone and check for system updates."
    },

    "Bluetooth not working": {
        "cause": "Bluetooth is disabled or there is a pairing problem.",
        "solution": "Turn Bluetooth on and pair the device again."
    },

    "Camera not opening": {
        "cause": "Camera application error or temporary system issue.",
        "solution": "Restart the phone or clear the camera app cache."
    },

    "Flashlight not working": {
        "cause": "Low battery or temporary software issue.",
        "solution": "Charge the phone and restart it."
    },

    "Mobile data not working": {
        "cause": "Mobile data is disabled or network signal is weak.",
        "solution": "Turn on mobile data and check the network signal."
    },

    "SIM card not detected": {
        "cause": "SIM card may be incorrectly inserted or damaged.",
        "solution": "Remove and reinsert the SIM card properly."
    },

    "Phone restarting automatically": {
        "cause": "Software problem or insufficient memory.",
        "solution": "Remove unnecessary applications and update the system."
    },

    "Touch screen not responding": {
        "cause": "Screen problem or temporary software lag.",
        "solution": "Restart the phone and check whether the screen responds."
    },

    "Fingerprint not working": {
        "cause": "Fingerprint sensor may be dirty or fingerprint data may not match.",
        "solution": "Clean the sensor and register the fingerprint again."
    },

    "Speaker problem": {
        "cause": "Low volume or speaker blockage.",
        "solution": "Increase the volume and gently clean the speaker area."
    },

    "Phone hanging frequently": {
        "cause": "Low memory or too many applications running.",
        "solution": "Close unnecessary applications and free storage space."
    }
}


# ============================================================
# DIAGNOSIS
# ============================================================

def diagnose():

    problem = problem_box.get()

    if problem == "Select a problem":
        messagebox.showwarning(
            "Select Problem",
            "Please select a mobile phone problem."
        )
        return

    # Rule matching / inference
    result = rules[problem]

    selected_label.config(
        text="Selected Problem: " + problem
    )

    cause_label.config(
        text=result["cause"]
    )

    solution_label.config(
        text=result["solution"]
    )

    status_label.config(
        text="✓ Diagnosis completed successfully"
    )


# ============================================================
# CLEAR
# ============================================================

def clear_result():

    problem_box.set("Select a problem")

    selected_label.config(
        text="Selected Problem: None"
    )

    cause_label.config(
        text="Select a problem and click Diagnose."
    )

    solution_label.config(
        text="Recommended solution will appear here."
    )

    status_label.config(
        text="Ready for diagnosis"
    )


# ============================================================
# VIEW 20 RULES
# ============================================================

def show_rules():

    rules_window = tk.Toplevel(root)

    rules_window.title(
        "Expert System - 20 Rules"
    )

    rules_window.geometry(
        "1050x650"
    )

    rules_window.configure(
        bg="#eef3f8"
    )

    # ---------------- HEADER ----------------

    header = tk.Frame(
        rules_window,
        bg="#1f4e79"
    )

    header.pack(
        fill="x"
    )

    title = tk.Label(
        header,
        text="📋 Knowledge Base - 20 Troubleshooting Rules",
        font=("Arial", 20, "bold"),
        bg="#1f4e79",
        fg="white",
        pady=15
    )

    title.pack()

    # ---------------- TABLE FRAME ----------------

    table_frame = tk.Frame(
        rules_window,
        bg="#eef3f8"
    )

    table_frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    # ---------------- SCROLLBARS ----------------

    vertical_scroll = ttk.Scrollbar(
        table_frame,
        orient="vertical"
    )

    horizontal_scroll = ttk.Scrollbar(
        table_frame,
        orient="horizontal"
    )

    # ---------------- TABLE ----------------

    columns = (
        "Rule",
        "Problem",
        "Possible Cause",
        "Solution"
    )

    table = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings",
        yscrollcommand=vertical_scroll.set,
        xscrollcommand=horizontal_scroll.set
    )

    vertical_scroll.config(
        command=table.yview
    )

    horizontal_scroll.config(
        command=table.xview
    )

    # ---------------- HEADINGS ----------------

    table.heading(
        "Rule",
        text="Rule"
    )

    table.heading(
        "Problem",
        text="Problem"
    )

    table.heading(
        "Possible Cause",
        text="Possible Cause"
    )

    table.heading(
        "Solution",
        text="Solution"
    )

    # ---------------- COLUMN WIDTHS ----------------

    table.column(
        "Rule",
        width=70,
        anchor="center"
    )

    table.column(
        "Problem",
        width=220
    )

    table.column(
        "Possible Cause",
        width=350
    )

    table.column(
        "Solution",
        width=400
    )

    # ---------------- INSERT 20 RULES ----------------

    for number, (problem, data) in enumerate(
        rules.items(),
        start=1
    ):

        table.insert(
            "",
            "end",
            values=(
                f"R{number}",
                problem,
                data["cause"],
                data["solution"]
            )
        )

    # ---------------- TABLE POSITION ----------------

    table.grid(
        row=0,
        column=0,
        sticky="nsew"
    )

    vertical_scroll.grid(
        row=0,
        column=1,
        sticky="ns"
    )

    horizontal_scroll.grid(
        row=1,
        column=0,
        sticky="ew"
    )

    table_frame.rowconfigure(
        0,
        weight=1
    )

    table_frame.columnconfigure(
        0,
        weight=1
    )

    # ---------------- INFORMATION ----------------

    info = tk.Label(
        rules_window,
        text="Total Rules: 20   |   Rule Type: IF-THEN   |   Knowledge Base",
        font=("Arial", 11, "bold"),
        bg="#eef3f8",
        fg="#1f4e79",
        pady=10
    )

    info.pack()


# ============================================================
# ABOUT
# ============================================================

def show_about():

    messagebox.showinfo(
        "About Project",
        "MOBILE PHONE TROUBLESHOOTING EXPERT SYSTEM\n\n"

        "This is a rule-based expert system developed "
        "using Python and Tkinter.\n\n"

        "The system uses 20 IF-THEN troubleshooting rules "
        "to identify possible causes and recommend solutions "
        "for common mobile phone problems.\n\n"

        "Technology:\n"
        "Python + Tkinter\n\n"

        "Knowledge Base:\n"
        "20 Troubleshooting Rules\n\n"

        "Project Type:\n"
        "Artificial Intelligence - Expert System"
    )


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title(
    "Mobile Phone Troubleshooting Expert System"
)

root.geometry(
    "950x700"
)

root.resizable(
    False,
    False
)

root.configure(
    bg="#eef3f8"
)


# ============================================================
# HEADER
# ============================================================

header = tk.Frame(
    root,
    bg="#1f4e79",
    height=120
)

header.pack(
    fill="x"
)

title = tk.Label(
    header,
    text="📱 Mobile Phone Troubleshooting",
    font=("Arial", 27, "bold"),
    bg="#1f4e79",
    fg="white"
)

title.pack(
    pady=(20, 5)
)

subtitle = tk.Label(
    header,
    text="Rule-Based Expert System for Common Mobile Problems",
    font=("Arial", 13),
    bg="#1f4e79",
    fg="white"
)

subtitle.pack()


# ============================================================
# NAVIGATION BAR
# ============================================================

nav_frame = tk.Frame(
    root,
    bg="#dce6f1",
    height=50
)

nav_frame.pack(
    fill="x"
)


# View Rules button

rules_button = tk.Button(
    nav_frame,
    text="📋 View 20 Rules",
    command=show_rules,
    font=("Arial", 11, "bold"),
    bg="#dce6f1",
    fg="#1f4e79",
    relief="flat",
    cursor="hand2"
)

rules_button.pack(
    side="left",
    padx=25,
    pady=8
)


# About button

about_button = tk.Button(
    nav_frame,
    text="ℹ About",
    command=show_about,
    font=("Arial", 11, "bold"),
    bg="#dce6f1",
    fg="#1f4e79",
    relief="flat",
    cursor="hand2"
)

about_button.pack(
    side="right",
    padx=25,
    pady=8
)


# ============================================================
# MAIN CONTENT
# ============================================================

content = tk.Frame(
    root,
    bg="#eef3f8"
)

content.pack(
    fill="both",
    expand=True,
    padx=60,
    pady=25
)


# ============================================================
# SELECT PROBLEM
# ============================================================

select_label = tk.Label(
    content,
    text="Select Your Mobile Problem",
    font=("Arial", 18, "bold"),
    bg="#eef3f8",
    fg="#1f2937"
)

select_label.pack(
    pady=(5, 10)
)


problem_box = ttk.Combobox(
    content,
    values=list(rules.keys()),
    state="readonly",
    font=("Arial", 13),
    width=50
)

problem_box.set(
    "Select a problem"
)

problem_box.pack(
    pady=5
)


# ============================================================
# BUTTONS
# ============================================================

button_frame = tk.Frame(
    content,
    bg="#eef3f8"
)

button_frame.pack(
    pady=18
)


# Diagnose button

diagnose_button = tk.Button(
    button_frame,
    text="🔍 Diagnose Problem",
    command=diagnose,
    font=("Arial", 13, "bold"),
    bg="#1f4e79",
    fg="white",
    padx=25,
    pady=10,
    cursor="hand2"
)

diagnose_button.pack(
    side="left",
    padx=10
)


# Clear button

clear_button = tk.Button(
    button_frame,
    text="↻ Clear",
    command=clear_result,
    font=("Arial", 13, "bold"),
    bg="#777777",
    fg="white",
    padx=30,
    pady=10,
    cursor="hand2"
)

clear_button.pack(
    side="left",
    padx=10
)


# ============================================================
# SELECTED PROBLEM
# ============================================================

selected_label = tk.Label(
    content,
    text="Selected Problem: None",
    font=("Arial", 12, "bold"),
    bg="#eef3f8",
    fg="#1f4e79"
)

selected_label.pack(
    pady=5
)


# ============================================================
# RESULT TITLE
# ============================================================

result_title = tk.Label(
    content,
    text="🔍 Diagnosis Result",
    font=("Arial", 19, "bold"),
    bg="#eef3f8",
    fg="#1f2937"
)

result_title.pack(
    pady=(10, 12)
)


# ============================================================
# RESULT CARD
# ============================================================

result_frame = tk.Frame(
    content,
    bg="white",
    bd=1,
    relief="solid"
)

result_frame.pack(
    fill="x",
    padx=20
)


# ============================================================
# POSSIBLE CAUSE
# ============================================================

cause_heading = tk.Label(
    result_frame,
    text="⚠ Possible Cause",
    font=("Arial", 13, "bold"),
    bg="white",
    fg="#1f4e79",
    anchor="w"
)

cause_heading.pack(
    fill="x",
    padx=20,
    pady=(15, 5)
)


cause_label = tk.Label(
    result_frame,
    text="Select a problem and click Diagnose.",
    font=("Arial", 12),
    bg="white",
    fg="#333333",
    anchor="w",
    justify="left",
    wraplength=800
)

cause_label.pack(
    fill="x",
    padx=20,
    pady=(0, 15)
)


# ============================================================
# RECOMMENDED SOLUTION
# ============================================================

solution_heading = tk.Label(
    result_frame,
    text="💡 Recommended Solution",
    font=("Arial", 13, "bold"),
    bg="white",
    fg="#1f4e79",
    anchor="w"
)

solution_heading.pack(
    fill="x",
    padx=20,
    pady=(5, 5)
)


solution_label = tk.Label(
    result_frame,
    text="Recommended solution will appear here.",
    font=("Arial", 12),
    bg="white",
    fg="#333333",
    anchor="w",
    justify="left",
    wraplength=800
)

solution_label.pack(
    fill="x",
    padx=20,
    pady=(0, 20)
)


# ============================================================
# STATUS
# ============================================================

status_label = tk.Label(
    content,
    text="Ready for diagnosis",
    font=("Arial", 10, "italic"),
    bg="#eef3f8",
    fg="#666666"
)

status_label.pack(
    pady=12
)


# ============================================================
# FOOTER
# ============================================================

footer = tk.Label(
    root,
    text="Rule-Based Expert System  •  Python + Tkinter  •  20 Rules",
    font=("Arial", 10),
    bg="#dce6f1",
    fg="#555555",
    pady=8
)

footer.pack(
    fill="x"
)


# ============================================================
# START APPLICATION
# ============================================================

root.mainloop()