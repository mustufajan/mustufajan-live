document.addEventListener('DOMContentLoaded', function(){

    skills();
    const highlights = document.querySelector('#highlights')

    document.querySelector('#arrow_down').addEventListener('click', () => {
        highlights.style.display = 'block';
        const career = document.querySelector('#career');
        career.style.animationPlayState = 'running';
        career.scrollIntoView({
            behavior: 'smooth',
        });
        on_scroll();
        document.querySelector('#arrow_down').style.display = 'none';
    });
    
    document.querySelector('#career_nav').onclick = () => {
        highlights.style.display = 'block';
        const career = document.querySelector('#career');
        career.style.animationPlayState = 'running';
        career.scrollIntoView({
            behavior: 'smooth',
        });
        on_scroll();
        document.querySelector('#arrow_down').style.display = 'none';
    }

    document.querySelector('#education_nav').onclick = () => {
        highlights.style.display = 'block';
        const education = document.querySelector('#education');
        document.querySelector('#career').style.animationPlayState = 'running';
        education.style.animationPlayState = 'running';
        education.scrollIntoView({
            behavior: 'smooth',
        });
        on_scroll();
        document.querySelector('#arrow_down').style.display = 'none';
    }

    document.querySelector('#projects_nav').onclick = () => {
        highlights.style.display = 'block';
        const projects = document.querySelector('#projects');
        document.querySelector('#career').style.animationPlayState = 'running';
        document.querySelector('#education').style.animationPlayState = 'running';
        projects.style.animationPlayState = 'running';
        projects.scrollIntoView({
            behavior: 'smooth',
        });
        on_scroll();
        document.querySelector('#arrow_down').style.display = 'none';
    }

    document.querySelector('#skills_nav').onclick = () => {
        highlights.style.display = 'block';
        show_highlights();
        const contact = document.querySelector('#contact');
        contact.style.animationPlayState = 'running';
        const skills = document.querySelector('#skills');
        skills.scrollIntoView({
            behavior: 'smooth',
        });
        
        document.querySelector('#arrow_down').style.display = 'none';
    }  

    /*document.querySelector('#contact_nav').onclick = () => {
        highlights.style.display = 'block';
        show_highlights();
        const contact = document.querySelector('#contact');
        contact.style.animationPlayState = 'running';
        contact.scrollIntoView({
            behavior: 'smooth',
        });
        
        document.querySelector('#arrow_down').style.display = 'none';
    }*/
    
    $(document).ready(function(){

        //pause the video once modal is hidden
        $(".modal").on('hidden.bs.modal', function () {
               video = $(this).find('iframe');
               video.attr('src', video.attr('src'));
        });

        //fix the modal background issue
        $(".modal").on('show.bs.modal', function () {
            $(this).appendTo("body") ;
        });

    });

})
   
function skills(){
    const starTotal = 5;
    fetch('/skills')
        .then(response => response.json())
        .then(skills => {
            var i=0;
            for(i=0; i<skills.length; i++){

                const starPercentage = (skills[i].level / starTotal) * 100;
                const starPercentageRounded = `${(Math.round(starPercentage / 10) * 10)}%`;
                document.querySelector( `#skill_${skills[i].id} .stars-inner`).style.width = starPercentageRounded;
            }
        })
}

function show_highlights(){
    document.querySelector('#career').style.animationPlayState = 'running';
    document.querySelector('#education').style.animationPlayState = 'running';
    document.querySelector('#projects').style.animationPlayState = 'running';
    document.querySelector('#skills').style.animationPlayState = 'running';
}

function on_scroll(){

    const education = document.querySelector('#education')
    const projects = document.querySelector('#projects')
    const skills = document.querySelector('#skills')
    const contact = document.querySelector('#contact')

    window.onscroll = () => {
        if(window.scrollY + window.innerHeight >= education.offsetTop){
            education.style.animationPlayState = 'running';
        };

        if(window.scrollY + window.innerHeight >= projects.offsetTop){
            projects.style.animationPlayState = 'running';
        };

        if(window.scrollY + window.innerHeight >= skills.offsetTop){
            skills.style.animationPlayState = 'running';
        };

        if(window.scrollY + window.innerHeight >= contact.offsetTop){
            contact.style.animationPlayState = 'running';
        };
    };
}