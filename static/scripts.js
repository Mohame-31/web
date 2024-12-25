async function fetchPosts() {
    const response = await fetch('/posts');
    const posts = await response.json();
    const postsDiv = document.getElementById('posts');
    postsDiv.innerHTML = '';
    posts.forEach(post => {
        const postDiv = document.createElement('div');
        postDiv.className = 'post';
        postDiv.innerHTML = `<strong>${post.user}</strong>: ${post.content}`;
        postsDiv.appendChild(postDiv);
    });
}

document.getElementById('postForm').onsubmit = async (e) => {
    e.preventDefault();
    const user = document.getElementById('user').value;
    const content = document.getElementById('content').value;
    await fetch('/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user, content })
    });
    fetchPosts();
    document.getElementById('postForm').reset();
};

fetchPosts();
