<script>
function resetSlideScrolling(slide) {
    slide.classList.remove('scrollable-slide');
}

function handleSlideScrolling(slide) {
    if (slide.scrollHeight >= 700) {
        slide.classList.add('scrollable-slide');
    }
}

Reveal.addEventListener('ready', function (event) {
    handleSlideScrolling(event.currentSlide);
});

Reveal.addEventListener('slidechanged', function (event) {
    if (event.previousSlide) {
        resetSlideScrolling(event.previousSlide);
    }
    handleSlideScrolling(event.currentSlide);
});
</script>