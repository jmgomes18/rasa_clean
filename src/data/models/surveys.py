from collections import namedtuple

Surveys = namedtuple(
    "Surveys", "id owner_id author_id status value time_elapsed created_at updated_at"
)
