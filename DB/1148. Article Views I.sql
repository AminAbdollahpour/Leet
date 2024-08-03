select author_id  id from Views
where author_id = viewer_id
group by author_id , viewer_id
;
