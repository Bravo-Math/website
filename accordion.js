const sections = document.querySelectorAll("section")

sections.forEach(section => {
  const toggler = section.querySelector("div.toggler")
  const panel = section.querySelector("div.panel")

  toggler.addEventListener("click", function (event) {
    section.classList.toggle("open")

          event.preventDefault()

    if (panel.style.maxHeight) {
      panel.style.maxHeight = null
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px"

    }
  })

})
