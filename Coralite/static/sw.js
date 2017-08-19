importScripts('/cache-polyfill.js');

self.addEventListener('install', function(e) {
 e.waitUntil(
   caches.open('coralite').then(function(cache) {
     return cache.addAll([
       '/'
     ]);
   })
 );
});