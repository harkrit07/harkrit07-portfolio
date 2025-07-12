const username = "harkrit07";
const container = document.getElementById("projects-container");

fetch(`https://api.github.com/users/${username}/repos`)
  .then(res => res.json())
  .then(repos => {
    repos.forEach(repo => {
      const div = document.createElement('div');
      div.className = 'project';
      div.innerHTML = `
        <h3>${repo.name}</h3>
        <p>${repo.description || "No description available."}</p>
        <a href="${repo.html_url}" target="_blank">View on GitHub</a>
      `;
      container.appendChild(div);
    });
  });

  



  