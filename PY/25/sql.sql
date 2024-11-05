select count(1) from artists
select ArtistId, name, * from artists LIMIT 1000


select * from artists as ar
inner join albums as al on al.ArtistId = ar.ArtistId
order by ArtistId

select al.title, tr.name from albums as al
inner join tracks as tr on tr.AlbumId= al.AlbumId
order by al.AlbumId


select ar.name, count(1), max(al.title) from artists ar
inner join albums al on al.ArtistId = ar.ArtistId
group by ar.ArtistId
order by count(1) desc

select ar.name, count(1), sum(tr.UnitPrice) from artists ar
inner join albums al on al.ArtistId = ar.ArtistId
inner join tracks tr on tr.AlbumId = al.AlbumId
group by ar.ArtistId
order by count(1) desc


