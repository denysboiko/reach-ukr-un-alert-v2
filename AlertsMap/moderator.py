from moderation import moderation
from moderation.moderator import GenericModerator
from moderation.db import ModeratedModel
from AlertsMap.models import Alert

class AlertModerator(GenericModerator):
    # notify_user = False
    auto_approve_for_staff = False


# moderation.register(Alert)  # Uses default moderation settings
moderation.register(Alert, AlertModerator)  # Uses custom mode