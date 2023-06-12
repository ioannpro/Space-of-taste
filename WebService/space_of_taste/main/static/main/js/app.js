
// Animation

const header = gsap.timeline({defaults: {duration: 2}});
const intro__img = gsap.timeline({defaults: {duration: 2}});
const intro__text = gsap.timeline({defaults: {duration: 1.5}});
const category = gsap.timeline({defaults: {duration: 4}});

header.from('.header', { opacity: 0, y: -130});

intro__img.from('#intro-pizza', { opacity: 0, rotate: 135, x: 1000});

intro__text.from('.intro__tittle', { opacity: 0, y: 100})
            .from('.intro__subtittle', { opacity: 0, y: 40})
            .from('.intro__subsub', { opacity: 0, y: 40})
            .from('.intro__btn', { opacity: 0, y: 40});

category.from('.category__a', { opacity: -1});