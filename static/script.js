const cardContainer = document.querySelector(".card-container");
const selectedDateInput = document.getElementById("selected-date");
const inName = document.getElementById("name");
const inPhone = document.getElementById("phone");
const inCompleain = document.getElementById("compleain");



const loadDefult = function () {
    const storedName = localStorage.getItem("name");
    const storedDate = localStorage.getItem("date");
    const storedPhone = localStorage.getItem("phone");
    const storedCompleain = localStorage.getItem("compleain");
    if (storedName && inName)
        inName.value = storedName;
    if (storedDate && selectedDateInput)
        selectedDateInput.value = storedDate;
    if (storedPhone && inPhone)
        inPhone.value = storedPhone;
    if (storedCompleain && inCompleain)
        inCompleain.value = storedCompleain;
}


if (cardContainer) {
    cardContainer.addEventListener('click', function (event) {
        if (event.target.classList.contains('completed')) {
            const cardToHide = event.target.closest(".card"); // Find closest ancestor with class "card"
            if (cardToHide) {
                const id = cardToHide.firstChild.nextElementSibling.innerHTML.trim()
                cardToHide.classList.add('hidden');
                deleteItem(id)
            }
            cardToHide.addEventListener('transitionend', function () {
                cardToHide.parentNode.removeChild(cardToHide); // Remove from DOM 
                cardToHide.style.display = "none"
            });
        }
    });
}

function deleteItem(id) {
    window.location.href = `/delete?id=${id}`
}

if (selectedDateInput) {
    selectedDateInput.addEventListener('change', function () {
        const selectedDate = this.value;
        localStorage.setItem("name", inName.value);
        localStorage.setItem("phone", inPhone.value);
        localStorage.setItem("compleain", inCompleain.value);
        localStorage.setItem("date", selectedDate);
        window.location.href = `/date?d=${selectedDate}`

    });
}


loadDefult();

