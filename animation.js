const animatedItem = document.querySelectorAll( ".drawings" )

animatedItem.forEach(tag => {
  tag.style.opacity = 0
})

const fadeIn = function () {
  let delay = 0.4  
  
  animatedItem.forEach(tag => {
    const tagTop = tag.getBoundingClientRect().top
    const tagBottom = tag.getBoundingClientRect().bottom
    
    if (window.getComputedStyle(tag).opacity == 0) {
      tag.style.animation = `fadein .625s ${delay}s both`
      delay = delay + 0.25
    }
  })
}

fadeIn()
