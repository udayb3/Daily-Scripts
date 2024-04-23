// Use this in the console of any browser to get a list of links.
container=request.document.getElementById('playlist').children[0]
items= container.children[2]
child= items.children
console.log(child)
ID={}
n_videos=child.length
for(var i=0;i<n_videos;i++)
 {
	anchor=child[i].children[0]
// Splitting with &
	link=anchor['href']
  ID[i]=link
}
console.log(ID)
