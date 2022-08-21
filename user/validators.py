import string
from django.core.exceptions import ValidationError


def contains_special_character(value):
    for char in value:
        if char in string.punctuation:
            return True
    return False


# 실습으로 완성해 주세요
def contains_uppercase_letter(value):
    for char in value:
        if char in string.ascii_uppercase:
            #print("대문자")
            return True
    return False


# 실습으로 완성해 주세요
def contains_lowercase_letter(value):
    for char in value:
        if char in string.ascii_lowercase:
            #print("소문자")
            return True
    return False


# 실습으로 완성해 주세요
def contains_number(value):
    for char in value:
        if char in string.digits:
            #print("숫자")
            return True
    return False


class CustomPasswordValidator:  #비밀번호는 클래스형태
    def validate(self, password, user=None):
        if (
                len(password) < 8 or
                not contains_uppercase_letter(password) or
                not contains_lowercase_letter(password) or
                not contains_number(password) or
                not contains_special_character(password)
        ):
            raise ValidationError("8자 이상의 영문 대/소문자, 숫자, 특수문자 조합이어야 합니다.")

    def get_help_text(self):
        return "8자 이상의 영문 대/소문자, 숫자, 특수문자 조합을 입력해 주세요."
        

def validate_no_special_characters(value):
    if contains_special_character(value):
        raise ValidationError("특수문자를 포함할 수 없습니다.")