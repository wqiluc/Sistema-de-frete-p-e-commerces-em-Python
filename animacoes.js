document.querySelectorAll("img.icon").forEach(icon => {
    icon.addEventListener("click", function (e) {
        e.preventDefault();
        const link = this.parentElement.href;
        this.classList.add("clicando");
        setTimeout(() => {
            window.open(link, "_blank");
            this.classList.remove("clicando");
        }, 220)});});