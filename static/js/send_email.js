function sendMail(name, email, message) {
    emailjs.send( "Email service", "template_ms3",{
        "from_name": name,
        "message": message,
        "from_email": email,
        })

        // Notify the users in case the message was successfully sent or not
        .then(
            // Function that notify the users in case the message was successfully sent
            function(response) {
                let form = document("message_response");
                let replacement = form.innerHTML = "<h5>Sent! Thank you for your message!</h5>";
            },
            // Function that lets users know in case the message was not sent
            function(error) {
                let form = document("message_response");

                form.innerHTML = "<h5>We encountered an error! Please try again.</h5>";
            });
        return false;
}

window.onload = function() {
    const submitBtn = document.querySelector('#submit');
    const nameBox = document.querySelector('#name');
    const emailBox = document.querySelector('#email');
    const MsgBox = document.querySelector('#message');

    submitBtn.addEventListener('click', function(event) {
        // This will prevent the default action of the form and then calls the sendMsg function
        event.preventDefault();
        sendMsg();
    });

    function sendMsg() {
        let nameContent = nameBox.value;
        let emailContent = emailBox.value;
        let MsgContent = MsgBox.value;

        // Alerts pop up if a required field has not been completed before pressing on the submit button
        if (nameContent === '') {
            alert('Please introduce your name.');
        }
        else if (emailContent === '') {
            alert('Please introduce your email address.');
        }
        else if (MsgContent === '') {
            alert('Please write here your message.');
        }
        // The sendMail function gets called if each of the required fields on the page have been completed
        else {
            sendMail(nameContent, emailContent, MsgContent);
        }
    }
}
