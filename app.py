from flask import Flask, render_template, request

app = Flask(__name__)

rules = {
    "Battery draining fast": {
        "cause": "Background apps or high battery usage",
        "solution": "Close unnecessary background apps and reduce battery usage"
    },
    "Phone overheating": {
        "cause": "Heavy apps or continuous usage",
        "solution": "Close heavy apps and allow the phone to cool down"
    },
    "Network not working": {
        "cause": "Weak signal or Airplane mode enabled",
        "solution": "Check Airplane mode and move to an area with better signal"
    },
    "Wi-Fi not connecting": {
        "cause": "Wi-Fi or router problem",
        "solution": "Reconnect Wi-Fi or restart the router"
    },
    "Storage full": {
        "cause": "Too many files or applications",
        "solution": "Delete unnecessary files and uninstall unused applications"
    },
    "Phone is slow": {
        "cause": "Low storage or too many background apps",
        "solution": "Free storage and close unnecessary apps"
    },
    "Apps crashing": {
        "cause": "Outdated or corrupted application",
        "solution": "Update or reinstall the application"
    },
    "Phone not charging": {
        "cause": "Charger, cable, or charging port problem",
        "solution": "Check the charger and cable and use a compatible charger"
    },
    "No sound": {
        "cause": "Silent mode or low volume",
        "solution": "Disable silent mode and increase the volume"
    },
    "Screen freezing": {
        "cause": "Application or system problem",
        "solution": "Restart the phone and check for system updates"
    },
    "Bluetooth not working": {
        "cause": "Bluetooth disabled or pairing problem",
        "solution": "Turn on Bluetooth and pair the device again"
    },
    "Camera not opening": {
        "cause": "Camera application or system error",
        "solution": "Restart the phone and clear the camera app cache"
    },
    "Flashlight not working": {
        "cause": "Low battery or software issue",
        "solution": "Charge the phone and restart it"
    },
    "Mobile data not working": {
        "cause": "Mobile data disabled or weak signal",
        "solution": "Enable mobile data and check the network signal"
    },
    "SIM card not detected": {
        "cause": "SIM inserted incorrectly or damaged",
        "solution": "Remove and reinsert the SIM card correctly"
    },
    "Phone restarting automatically": {
        "cause": "Software or memory problem",
        "solution": "Remove unnecessary apps and update the system"
    },
    "Touch screen not responding": {
        "cause": "Screen or software lag",
        "solution": "Restart the phone and check the screen"
    },
    "Fingerprint not working": {
        "cause": "Dirty sensor or fingerprint mismatch",
        "solution": "Clean the sensor and register the fingerprint again"
    },
    "Speaker problem": {
        "cause": "Low volume or speaker blockage",
        "solution": "Increase volume and clean the speaker area"
    },
    "Phone hanging frequently": {
        "cause": "Low memory or too many applications",
        "solution": "Close unnecessary apps and free storage"
    }
}


@app.route("/", methods=["GET", "POST"])
def home():
    selected_problem = ""
    diagnosis = None

    if request.method == "POST":
        selected_problem = request.form.get("problem", "")
        if selected_problem in rules:
            diagnosis = rules[selected_problem]

    return render_template(
        "index.html",
        rules=rules,
        selected_problem=selected_problem,
        diagnosis=diagnosis
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )