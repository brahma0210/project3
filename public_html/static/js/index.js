async function calculate(form) {
    event.preventDefault();
    const options = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            num1: parseInt(form.num1.value),
            num2: parseInt(form.num2.value),
            type: form.type.value
        })
    }
    const request = await fetch("/calculate", options);
    const response = await request.json();
    if (response.success) {
        const resultDiv = document.querySelector(".result");
        resultDiv.style.color = "black";
        resultDiv.innerText = response.result;
    } else {
        const resultDiv = document.querySelector(".result");
        resultDiv.style.color = "red";
        resultDiv.innerText = response.error;
    }
}