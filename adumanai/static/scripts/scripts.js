// document.addEventListener("DOMContentLoaded", function() {
//     const slides = document.querySelectorAll('.slider img');
//     let currentSlide = 0;
//     const slideInterval = 3000; // Change slide every 3 seconds

//     function showNextSlide() {
//         slides[currentSlide].classList.remove('active');
//         currentSlide = (currentSlide + 1) % slides.length;
//         slides[currentSlide].classList.add('active');
//     }

//     setInterval(showNextSlide, slideInterval);
// }); 

//   document.addEventListener('DOMContentLoaded', function() {
//     const slider = document.getElementsByClassName('slider');
//     const slides = slider.children;
//     const slideCount = slides.length;
//     let currentIndex = 0;
//     const slideIntervalTime = 5000; // 5 seconds
//     let slideInterval;

//     // Function to move to the next slide
//     function nextSlide() {
//       currentIndex = (currentIndex + 1) % slideCount;
//       slider.scrollTo({
//         left: slider.clientWidth * currentIndex,
//         behavior: 'smooth'
//       });
//     }

//     // Start the slideshow
//     function startSlideShow() {
//       slideInterval = setInterval(nextSlide, slideIntervalTime);
//     }

//     // Stop the slideshow
//     function stopSlideShow() {
//       clearInterval(slideInterval);
//     }

//     // Initialize the slideshow
//     startSlideShow();

//     // Pause the slideshow when user hovers over the slider
//     slider.addEventListener('mouseenter', stopSlideShow);
//     slider.addEventListener('mouseleave', startSlideShow);

//     // Adjust the scroll position when the window is resized
//     window.addEventListener('resize', function() {
//       slider.scrollTo({
//         left: slider.clientWidth * currentIndex,
//         behavior: 'smooth'
//       });
//     });
//   });

// document.addEventListener('DOMContentLoaded', function() {
//     const slides = document.querySelectorAll('.slider img');
//     let currentIndex = 0;
//     const slideIntervalTime = 2500; // 5 seconds
//     let slideInterval;
  
//     // Function to move to the next slide
//     function nextSlide() {
//       slides[currentIndex].classList.remove('active');
//       currentIndex = (currentIndex + 1) % slides.length;
//       slides[currentIndex].classList.add('active');
//     }
  
//     // Start the slideshow
//     function startSlideShow() {
//       slideInterval = setInterval(nextSlide, slideIntervalTime);
//     }
  
//     // Stop the slideshow
//     function stopSlideShow() {
//       clearInterval(slideInterval);
//     }
  
//     // Initialize the slideshow
//     startSlideShow();
  
//     // Get the slider container
//     const sliderContainer = document.querySelector('.slider-container');
  
//     // Pause the slideshow when user hovers over the slider container
//     sliderContainer.addEventListener('mouseenter', stopSlideShow);
  
//     // Resume the slideshow when user leaves the slider container
//     sliderContainer.addEventListener('mouseleave', startSlideShow);
//   });
  

document.addEventListener('DOMContentLoaded', function() {
    const slider = document.querySelector('.slider');
    const slides = document.querySelectorAll('.slider img');
    let currentIndex = 0;
    const slideIntervalTime = 2500; // 5 seconds
    let slideInterval;
  
    // Function to move to the next slide
    function nextSlide() {
      // Calculate the next index
      const nextIndex = (currentIndex + 1) % slides.length;
  
      // Slide out the current slide to the left and slide in the next slide from the right
      slider.style.transform = `translateX(-${nextIndex * 100}%)`;
  
      // Update the current index
      currentIndex = nextIndex;
    }
  
    // Start the slideshow
    function startSlideShow() {
      slideInterval = setInterval(nextSlide, slideIntervalTime);
    }
  
    // Stop the slideshow
    function stopSlideShow() {
      clearInterval(slideInterval);
    }
  
    // Initialize the slideshow
    startSlideShow();
  
    // Get the slider container
    const sliderContainer = document.querySelector('.slider-container');
  
    // Pause the slideshow when user hovers over the slider container
    sliderContainer.addEventListener('mouseenter', stopSlideShow);
  
    // Resume the slideshow when user leaves the slider container
    sliderContainer.addEventListener('mouseleave', startSlideShow);
  });
  