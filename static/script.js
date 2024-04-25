const cardContainer = document.querySelector(".card-container");
//const btn = document.querySelector(".completed");
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
            //cardToHide.style.display = "none"
        });
    }
});

function deleteItem(id) {
    window.location.href = `/delete?id=${id}`
}

