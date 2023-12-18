from django.shortcuts import get_object_or_404
from ninja import File, Router, FormEx
from ninja.files import UploadedFile
from typing import List, Union
from users.models import *
from messaging.models import *
from schemas.messaging import *
from django.db.models import Q

router = Router(tags=["Polls, Options and Votes Endpoints"])

@router.get('list_all_polls/', response=List[PollRetrievalSchema])
def list_polls(request):
    """Get a list of all registered polls"""
    return Poll.objects.all()

@router.get('poll/{poll_id}/get/', response=Union[PollRetrievalSchema, str])
def poll(request, poll_id):
    """Get a specific poll details"""
    poll = get_object_or_404(Poll, id=poll_id)
    return poll


@router.post('poll/add', response=PollRetrievalSchema)
def create_poll(request, pollData:PollRegistrationSchema=FormEx(None)):
    """Create a new Poll"""
    poll = Poll.objects.create(**pollData.dict())
    return poll

@router.post('{poll_id}/poll_option/add', response=PollRetrievalSchema)
def create_poll_option(request, poll_id, pollOptionData:PollOptionRegistrationSchema=FormEx(None)):
    """Create a new Poll Option and add it to a poll with poll_id"""
    poll = get_object_or_404(Poll, id=poll_id)
    if poll:
        poll_option = PollOption.objects.create(**pollOptionData.dict())
        if poll_option:
            poll.options.add(poll_option)
            poll.save()
    return poll

@router.delete('poll/{poll_id}/delete/')
def delete_poll(request, poll_id):
    """Delete a specific poll"""
    poll = get_object_or_404(Poll, id=poll_id)
    if poll:
        poll.delete()
        return "Poll {poll.id} deleted successfully"
    return poll






# POLL OPTIONS


@router.get('list_all_poll_options/', response=List[PollOptionRetrievalSchema])
def list_poll_options(request):
    """Get a list of all registered poll options"""
    return PollOption.objects.all()

@router.get('poll_option/{poll_option_id}/get/', response=Union[PollOptionRetrievalSchema, str])
def poll_option(request, poll_option_id):
    """Get a specific poll option details"""
    poll_option = get_object_or_404(PollOption, id=poll_option_id)
    return poll_option
    
@router.get('{poll_id}/poll_options/get/', response=List[PollOptionRetrievalSchema])
def list_poll_options_for_poll(request, poll_id):
    """List all poll options for a particular poll"""
    poll = get_object_or_404(Poll, id=poll_id)
    return poll.options.all()



@router.delete('poll_option/{poll_option_id}/delete/')
def delete_poll_option(request, poll_option_id):
    """Delete a specific Poll Option"""
    poll_option = get_object_or_404(PollOption, id=poll_option_id)
    if poll_option:
        poll_option.delete()
        return "Poll Option {poll_option.id} deleted successfully"
    return poll_option





# POLL VOTE

@router.get('list_all_poll_votes/', response=List[PollVoteRetrievalSchema])
def list_poll_votes(request):
    """Get a list of all registered poll votes"""
    return PollVote.objects.all()

@router.get('poll_vote/{poll_vote_id}/get/', response=Union[PollVoteRetrievalSchema, str])
def poll_vote(request, poll_vote_id):
    """Get a specific poll vote details"""
    poll_vote = get_object_or_404(PollVote, id=poll_vote_id)
    return poll_vote

@router.get('poll_vote/{poll_id}/get/', response=List[PollVoteRetrievalSchema])
def get_poll_vote_list_for_poll(request, poll_id):
    """Get poll votes list for a particular poll"""
    poll_votes = PollVote.objects.filter(poll_id=poll_id)
    return poll_votes


@router.get('poll_vote/{selected_option_id}/get/', response=List[PollVoteRetrievalSchema])
def get_poll_vote_list_for_poll_option(request, selected_option_id):
    """Get poll votes list for a particular poll option"""
    poll_votes = PollVote.objects.filter(selected_option_id=selected_option_id)
    return poll_votes


@router.post('poll_vote/add', response=PollVoteRetrievalSchema)
def create_poll_vote(request, pollVoteData:PollVoteRegistrationSchema=FormEx(None)):
    """Create a new Poll Vote"""
    poll_vote = PollVote.objects.create(**pollVoteData.dict())
    return poll_vote


@router.delete('poll_vote/{poll_vote_id}/delete/')
def delete_poll_vote(request, poll_vote_id):
    """Delete a specific Poll Vote"""
    poll_vote = get_object_or_404(PollVote, id=poll_vote_id)
    if poll_vote:
        poll_vote.delete()
        return "Poll Vote {poll_vote.id} deleted successfully"
    return poll_vote
