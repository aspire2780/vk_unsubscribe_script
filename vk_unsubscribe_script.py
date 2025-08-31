import vk_api
import time
from vk_api.exceptions import ApiError

def unsubscribe_from_all_groups():
    
    TOKEN = 'YOUR_ACCESS_TOKEN_HERE' 
    
    
    vk_session = vk_api.VkApi(token=TOKEN)
    vk = vk_session.get_api()
    
    try:
        print("получаем список групп...")
        groups = vk.groups.get(extended=1, count=1000)
        
        total_groups = groups['count']
        group_items = groups['items']
        
        print(f"найдено групп: {total_groups}")
        
        if total_groups == 0:
            print("вы не подписаны ни на одну группу.")
            return
        
        confirm = input(f"вы уверены, что хотите отписаться от всех {total_groups} групп? (да/нет): ")
        if confirm.lower() not in ['да', 'yes', 'y']:
            print("операция отменена.")
            return
        
        unsubscribed_count = 0
        errors_count = 0
        
        for i, group in enumerate(group_items, 1):
            group_id = group['id']
            group_name = group['name']
            
            try:
                vk.groups.leave(group_id=group_id)
                unsubscribed_count += 1
                print(f"[{i}/{total_groups}] отписались от: {group_name}")
                
                time.sleep(0.5)
                
            except ApiError as e:
                errors_count += 1
                print(f"[{i}/{total_groups}] ошибка при отписке от {group_name}: {e}")
                time.sleep(1)
            
            except Exception as e:
                errors_count += 1
                print(f"[{i}/{total_groups}] неожиданная ошибка для {group_name}: {e}")
                time.sleep(1)
        

        print(f"\n=== готово ===")
        print(f"успешно отписались: {unsubscribed_count}")
        print(f"ошибок: {errors_count}")
        print(f"всего обработано: {total_groups}")
        
    except ApiError as e:
        print(f"вшибка vk api: {e}")
    except Exception as e:
        print(f"общая ошибка: {e}")

if __name__ == "__main__":
    print("=== скрипт отписки от всех групп ВК_By_Petyablatnoy ===")
    print("ВНИМАНИЕ: этот скрипт отпишет вас от ВСЕХ групп!")
    print("сохраните нужные\n")
    
    unsubscribe_from_all_groups()
