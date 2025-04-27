document.addEventListener('DOMContentLoaded', function() {
    const currentUrl = window.location.pathname;
    
    if (currentUrl === "/new_post") { 
        document.querySelector('#cancel-post').onclick = handle_cancel_process
        document.querySelector('#compose-post-form').onsubmit = sent_post
    } else {
        load_posts();
    }
})

function load_posts() {
    document.querySelector('#post-view').style.display = 'block';
    
    fetch('/render_posts')
    .then(response => response.json())
    .then(posts => {
        if (posts.length === 0) {
            console.log("No posts here")
        } else {
            posts.forEach(post => {
                create_post_element(post)
            })
            
        }
    })
}



function handle_cancel_process () {
    redirectTo("")
   /*  document.querySelector('#cancel-post').addEventListener('click', () => {
        //load_posts();
    }) */
    return false
}

function sent_post() {
    fetch('/compose_post', {
        method: 'POST',
        body: JSON.stringify({
            content: `${document.querySelector('#text-field').value}`
        })
    })
    .then(response => response.json())
    .then(result => {
        //load_posts();
        redirectTo("")
        console.log("The content has been posted...")
    })
    .catch(error => {
        console.log("Error in the process of publish a new post is occured:", error)
    })

    console.log("this function is called!")
    return false
}

function create_post_element(post) {
    const post_element = document.createElement('li')

    post_element.innerHTML = `
        <span> ${post.author_name} </span>
        <p>${post.content}</p>
        <span> ${post.created_at} </span>
        <div>
            <img src="static/network/icons/heart.svg" alt="like icon" />
            <span> ${post.nb_of_likes === 0 ? '0' : post.nb_of_likes} </span>
            <span> ${post.nb_of_views === 0 ? '': post.nb_of_views} </span>
        </div>
        <span> Comment </span>
        <hr />
    `
    document.querySelector('#post-lists').append(post_element)
    
}

//when a user try to add a post and are note logged in, 
function create_popup_menu() {

}


function redirectTo(url) {
    window.location.pathname = url
}