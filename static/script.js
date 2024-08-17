
const guessInputField= document.querySelector("#text-input");

// handle button click

const handleClick=()=>{
    const input = Number(guessInputField.value.trim());
    fetch(`${window.origin}/play`,{
        method: "POST",
        body: input,
        credentials: "include",
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })

    }).then((response)=>{
        if (response.status != 200){
            console.log(`the response is not 200: ${response.status}`)
        }

        response.json().then((data)=>{
            // unpack data
            const {attempt, comment, guess, secret, wins} = data;
            // get elements that need updating
            const num_attempts_element = document.querySelector("#attempts");
            const guess_element = document.querySelector("#user-guess");
            const wins_element = document.querySelector("#wins");
            const message_element = document.querySelector("#game-message");

            // update elements
            num_attempts_element.innerHTML = data["attempts"];
            guess_element.innerHTML =  guess;
            wins_element.innerHTML = wins;
            message_element.innerHTML = comment;

            console.log(data)

        })

    })
    guessInputField.value ="";

}

const handleQuit=()=>{
fetch(`${window.origin}/quit`,{
    method: "POST",
    body: "",
    credentials: "include",
    cache: "no-cache",
    headers: new Headers({
        "content-type": "application/json"
    })

}).then((response)=>{
    if (response.status != 200){
        console.log(`the response is not 200: ${response.status}`)
    }

    response.json().then((data)=>{
        // unpack data
        const {attempt, comment, guess, secret, wins} = data;
        // get elements that need updating
        const num_attempts_element = document.querySelector("#attempts");
        const guess_element = document.querySelector("#user-guess");
        const wins_element = document.querySelector("#wins");
        const message_element = document.querySelector("#game-message");

        // update elements
        num_attempts_element.innerHTML = data["attempts"];
        guess_element.innerHTML =  guess;
        wins_element.innerHTML = wins;
        message_element.innerHTML = comment;

        console.log(data)

    })

})
guessInputField.value ="";

}

