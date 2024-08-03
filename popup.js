document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('discord-button').addEventListener('click', function () {
      chrome.tabs.create({ url: 'https://discord.gg/PXTtxEK7g8' });
    });
  
    document.getElementById('updates-button').addEventListener('click', function () {
      chrome.tabs.create({ url: 'https://github.com/mihai14launcher/OnPlayer' });
    });
  
    document.getElementById('tutorial-button').addEventListener('click', function () {
      chrome.tabs.create({ url: 'https://onplayer-vox.vercel.app/tutorial' });
    });
  });
  