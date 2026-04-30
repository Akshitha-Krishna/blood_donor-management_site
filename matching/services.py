
from donors.models import DonorProfile

def find_matching_donors(blood_group):
    return DonorProfile.objects.filter(
        blood_group=blood_group,
        available = True
    )