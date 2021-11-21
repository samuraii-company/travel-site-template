// menu callback
let navbar = document.querySelector('.header .navbar');

document.querySelector('#menu-btn').onclick = () =>{
    navbar.classList.toggle('active')
}

//video callback
document.querySelectorAll(".about .video-container .controls .control-btn").forEach(btn =>{
    btn.onclick = () => {
        let src = btn.getAttribute('data-src');
        document.querySelector(".about .video-container .video").src = src;
    }
})

let modal_container = document.getElementById("modal_container");

document.querySelectorAll("#form_btn").forEach(btn =>{
    btn.onclick = () =>{
        modal_container.classList.add("show")
    }
})

document.querySelector(".close").onclick= () =>{
    modal_container.classList.remove("show")
}

