document.addEventListener('DOMContentLoaded', function() {

    if (document.getElementById('#compose-post-view')) {
        document.querySelector('#add-new-post').addEventListener('click', () => load_compose_form_box())
        document.querySelector('#compose-post-form').onsubmit = sent_post 
    }
    load_posts();
})

function load_compose_form_box() {
    document.querySelector('#post-view').style.display = 'none';
    document.querySelector('#compose-post-view').style.display = 'block';
    document.querySelector('#add-new-post').style.display = 'none';

    handle_process();
}

function load_posts() {
    document.querySelector('#post-view').style.display = 'block';
    
    if(document.getElementById('#compose-post-view')) {
        document.querySelector('#compose-post-view').style.display = 'none';
        document.querySelector('#add-new-post').style.display = 'block';
    }

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



function handle_process () {
    document.querySelector('#cancel-post').addEventListener('click', () => {
        load_posts();
    })
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
        load_posts();
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
        <span> Foo </span>
        <p>${post.content}</p>
        <span> ${post.created_at} </span>
        <div>
            <span> ${post.nb_of_likes === 0 ? '' : post.nb_of_likes} </span>
            <span> ${post.nb_of_views === 0 ? '': post.nb_of_views} </span>
        </div>
        <span> Comment </span>
    `
    document.querySelector('#post-lists').append(post_element)
    
}