# square_sms_assistant
Text messaging assistant for Square merchants

## Description:

-   Square SMS Assistant (SSA) is an online bot hosted on a web server that listens for and processes incoming SMS messages, matches them to registered Square accounts in SSA, and provides API communication with the Square merchant backend. SMS functionality is done using Twilio
    -   The text message is sent from the user to a Twilio phone number
    -   Twilio is programmed to forward a text to an API endpoint on our web server
    -   Web server hosts a Flask instance that listens for incoming "texts" (API calls) from Twilio on an HTTP port
    -   An incoming Twilio call triggers Flask to launch logic that parses the incoming text for its phone number, matches it to a registered user, logs the text, and sends a reply based on the processing of the string in the text
    -   Most replies involve first making calls back to the Square API in order to retrieve merchant information
    -   Example: A small business owner wants to find out quick details about their business on the go. They can text  the "assistant" predetermined phrases to get bites of information back
        -   ie texting the assistant "list customers" sends back a text with the latest customers recorded by the merchant
-   Text processing logic is hard-coded to predetermined phrases in the prototype, but the next step would be to insert a layer of Natural Language Model that will translate spoken-word commands into the requisite API calls. This could likely be done using OpenAI's NML API
    -   Then it would be an "AI chat assistant"
