import csv
import os
from django.apps import apps
from django.core.management.base import BaseCommand
from django.db import models
from django.db.models import ForeignKey

class Command(BaseCommand):
    help = 'Insert data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')
# `python manage.py insert_csv path_to_csv_file` 명령어를 실행하면 `path_to_csv_file`가 `csv_file`에 저장됩니다. `add_arguments` 함수에서 `parser.add_argument('csv_file', type=str, help='Path to the CSV file')` 코드는 `insert_csv.py` 파일에서 `python manage.py insert_csv` 명령어를 실행할 때, `path_to_csv_file`와 같은 위치 인자를 받아서 `csv_file`에 저장하도록 정의한 부분입니다.
# 따라서, `python manage.py insert_csv path_to_csv_file` 명령어를 실행하면 `path_to_csv_file`가 `csv_file`에 저장되어 `handle` 함수에서 이를 사용하여 CSV 파일을 읽어들이고, Django 모델에 데이터를 추가합니다.

    def handle(self, *args, **options):
        csv_file = options['csv_file']
# `python manage.py insert_csv path_to_csv_file` 명령어를 실행할 때, `path_to_csv_file`는 위치 인자로서 `*args`에 저장됩니다. 따라서, `*args`는 `('path_to_csv_file',)`와 같은 튜플 형태로 저장됩니다.
# `**options`는 Django의 `BaseCommand` 클래스에서 상속받은 클래스에서 구현되는 함수에서 커맨드 라인 인터페이스를 통해 전달되는 인자들을 받는 매개변수입니다. `insert_csv.py` 파일에서 `handle` 함수에서는 `csv_file`이라는 이름의 위치 인자를 받지 않습니다. 대신, `**options`에서 `'csv_file'` 키를 사용하여 커맨드 라인에서 전달된 CSV 파일의 경로를 가져옵니다.
# 따라서, `*args`는 `('path_to_csv_file',)`와 같은 튜플 형태로 저장되고, `**options`는 `{'csv_file': 'path_to_csv_file'}`와 같은 딕셔너리 형태로 저장됩니다.


        app_label = 'main'  # Replace with your app label
        # Get all model classes for the app
        app_config = apps.get_app_config(app_label)
        models_config = app_config.get_models()

        class_mapping = {}
        for class_obj in models_config:
            class_name = class_obj.__name__
            class_mapping[class_name] = class_obj

        model_mapping = {
            'summoner_info.csv': class_mapping.get('Summoner_Info'),
            'league_info.csv': class_mapping.get('League_Info'),
            'time_info.csv': class_mapping.get('Time_Info'),
            'matchId.csv': class_mapping.get('MatchId'),
            'match.csv': class_mapping.get('Match'),
            'match_metadata.csv': class_mapping.get('Match_Metadata'),
            'match_info.csv': class_mapping.get('Match_Info'),
            'match_participantList.csv': class_mapping.get('Match_ParticipantList'),
            'match_participant1_info.csv': class_mapping.get('Match_Participant1_Info'),
            'match_participant2_info.csv': class_mapping.get('Match_Participant2_Info'),
            'match_participant3_info.csv': class_mapping.get('Match_Participant3_Info'),
            'match_participant4_info.csv': class_mapping.get('Match_Participant4_Info'),
            'match_participant5_info.csv': class_mapping.get('Match_Participant5_Info'),
            'match_participant6_info.csv': class_mapping.get('Match_Participant6_Info'),
            'match_participant7_info.csv': class_mapping.get('Match_Participant7_Info'),
            'match_participant8_info.csv': class_mapping.get('Match_Participant8_Info'),
            'match_participant9_info.csv': class_mapping.get('Match_Participant9_Info'),
            'match_participant10_info.csv': class_mapping.get('Match_Participant10_Info'),
            'match_participant1_challenges.csv': class_mapping.get('Match_Participant1_Challenges'),
            'match_participant2_challenges.csv': class_mapping.get('Match_Participant2_Challenges'),
            'match_participant3_challenges.csv': class_mapping.get('Match_Participant3_Challenges'),
            'match_participant4_challenges.csv': class_mapping.get('Match_Participant4_Challenges'),
            'match_participant5_challenges.csv': class_mapping.get('Match_Participant5_Challenges'),
            'match_participant6_challenges.csv': class_mapping.get('Match_Participant6_Challenges'),
            'match_participant7_challenges.csv': class_mapping.get('Match_Participant7_Challenges'),
            'match_participant8_challenges.csv': class_mapping.get('Match_Participant8_Challenges'),
            'match_participant9_challenges.csv': class_mapping.get('Match_Participant9_Challenges'),
            'match_participant10_challenges.csv': class_mapping.get('Match_Participant10_Challenges'),
            'match_participant1_perks.csv': class_mapping.get('Match_Participant1_Perks'),
            'match_participant2_perks.csv': class_mapping.get('Match_Participant2_Perks'),
            'match_participant3_perks.csv': class_mapping.get('Match_Participant3_Perks'),
            'match_participant4_perks.csv': class_mapping.get('Match_Participant4_Perks'),
            'match_participant5_perks.csv': class_mapping.get('Match_Participant5_Perks'),
            'match_participant6_perks.csv': class_mapping.get('Match_Participant6_Perks'),
            'match_participant7_perks.csv': class_mapping.get('Match_Participant7_Perks'),
            'match_participant8_perks.csv': class_mapping.get('Match_Participant8_Perks'),
            'match_participant9_perks.csv': class_mapping.get('Match_Participant9_Perks'),
            'match_participant10_perks.csv': class_mapping.get('Match_Participant10_Perks'),
            'match_participant1_statPerks.csv': class_mapping.get('Match_Participant1_StatPerks'),
            'match_participant2_statPerks.csv': class_mapping.get('Match_Participant2_StatPerks'),
            'match_participant3_statPerks.csv': class_mapping.get('Match_Participant3_StatPerks'),
            'match_participant4_statPerks.csv': class_mapping.get('Match_Participant4_StatPerks'),
            'match_participant5_statPerks.csv': class_mapping.get('Match_Participant5_StatPerks'),
            'match_participant6_statPerks.csv': class_mapping.get('Match_Participant6_StatPerks'),
            'match_participant7_statPerks.csv': class_mapping.get('Match_Participant7_StatPerks'),
            'match_participant8_statPerks.csv': class_mapping.get('Match_Participant8_StatPerks'),
            'match_participant9_statPerks.csv': class_mapping.get('Match_Participant9_StatPerks'),
            'match_participant10_statPerks.csv': class_mapping.get('Match_Participant10_StatPerks'),
            'match_participant1_perkStyles.csv': class_mapping.get('Match_Participant1_PerkStyles'),
            'match_participant2_perkStyles.csv': class_mapping.get('Match_Participant2_PerkStyles'),
            'match_participant3_perkStyles.csv': class_mapping.get('Match_Participant3_PerkStyles'),
            'match_participant4_perkStyles.csv': class_mapping.get('Match_Participant4_PerkStyles'),
            'match_participant5_perkStyles.csv': class_mapping.get('Match_Participant5_PerkStyles'),
            'match_participant6_perkStyles.csv': class_mapping.get('Match_Participant6_PerkStyles'),
            'match_participant7_perkStyles.csv': class_mapping.get('Match_Participant7_PerkStyles'),
            'match_participant8_perkStyles.csv': class_mapping.get('Match_Participant8_PerkStyles'),
            'match_participant9_perkStyles.csv': class_mapping.get('Match_Participant9_PerkStyles'),
            'match_participant10_perkStyles.csv': class_mapping.get('Match_Participant10_PerkStyles'),
            'match_teamsList.csv': class_mapping.get('Match_TeamsList'),
            'match_team0_info.csv': class_mapping.get('Match_Team0_Info'),
            'match_team1_info.csv': class_mapping.get('Match_Team1_Info'),
            'match_team0_bans.csv': class_mapping.get('Match_Team0_Bans'),
            'match_team1_bans.csv': class_mapping.get('Match_Team1_Bans'),
            'match_team0_objectives.csv': class_mapping.get('Match_Team0_Objectives'),
            'match_team1_objectives.csv': class_mapping.get('Match_Team1_Objectives'),
            'summonerId_matchId.csv': class_mapping.get('SummonerId_MatchId'),
        }
        
        filename = os.path.basename(csv_file)
        if filename not in model_mapping:
            self.stdout.write(f"{csv_file}does not exist in the model_mapping dictionary")
            return
        
        model_class = model_mapping[filename]
        if model_class == None:
            self.stdout.write(f"No matching model found for {csv_file}")
            return
        
        fields = [field.name for field in model_class._meta.fields if not field.name.endswith('_id')]  # api에서 받지않는 필드(필드명이 _id로 끝남)는 제외
        
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)  # Store the header row
            rows = list(reader)  # Convert remaining rows to a list. reader는 위에서 next(reader)했으므로 header를 제외한 나머지를 리스트로 반환.
            # print(header)
            # print(rows)

            for row_index, row in enumerate(rows):
            #   print(row)
            #     print(row_index)
            #     print(fields)
            #     break  
                data = {}
                for i, field_name in enumerate(fields):
                    field = model_class._meta.get_field(field_name)
                    if isinstance(field, ForeignKey):
                        related_model = field.related_model
                        # print(field_name)
                        # print(related_model)
                        # print(related_model.objects.all())
                        # print(related_model.objects.all()[row_index])
                        related_object, created = related_model.objects.get_or_create(**{field.remote_field.field_name: row[i]})  # field.remote_field.field_name은 현재 생성된 관련 모델의 필드 이름을 나타냅니다.

                    else:
                        model_object, created = model_class.objects.get_or_create(**{field_name: row[i]})  # **{field_name: row[i]}는 {field_name: row[i]}를 키워드 인수로 사용. → 모델객체가 이미 존재한다면 가져오고, 존재하지 않는다면 생성합니다.

'''
만약 위의 코드가 사용된 파일과 models.py 파일이 동일한 Django 앱에 속한다면,
model_mapping = {
    'summoner_info.csv': 'main.Summoner_Info',
    'league_info.csv': 'other_app.League_Info',
}
와 같이 앱 레이블과 모델 이름을 함께 지정하거나,
apps.get_model 메서드를 사용할 필요 없이 위의 코드를 그대로 사용할 수 있습니다.

앱 내에서 모델 클래스를 참조할 때, Django는 앱의 모델들을 자동으로 로드하고 사용할 수 있습니다. 따라서 model_mapping 딕셔너리에 직접 모델 클래스를 지정할 때, 앱 레이블을 추가로 지정할 필요 없이 모델 클래스의 이름만 사용하면 됩니다.

만약 Summoner_Info에 노란색 밑줄이 그어진다면, 일반적으로 개발 환경의 정적 분석기(static analyzer)가 해당 식별자를 찾을 수 없다는 의미입니다. 정적 분석기는 코드의 구문과 식별자를 분석하여 잠재적인 오류를 감지하고 표시하는 도구입니다.

노란색 밑줄은 정적 분석기가 잠재적인 오류를 가리키는 주의 표시입니다. 하지만 이는 단지 정적 분석기가 해당 식별자를 찾을 수 없다는 것을 의미하며, 실제로 코드를 실행할 때 문제가 발생하지는 않습니다.
따라서, 코드를 동일한 앱 내에서 사용한다면, Summoner_Info가 정의된 위치에 대한 정적 분석기의 경고는 무시해도 됩니다. 코드를 실행하면 정상적으로 동작할 것입니다.
'''