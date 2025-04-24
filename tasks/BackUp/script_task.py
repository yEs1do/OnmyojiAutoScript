# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
import locale
import os
import re
import shutil
from datetime import datetime

from module.exception import TaskEnd
from module.logger import logger, log_path, log_names, backup_path, week_path, delete_path, old_path, error_path
from tasks.base_task import BaseTask

""" 备份日志 """


class ScriptTask(BaseTask):
    # 动态生成需要排除的目录名集合
    exclude_dirs = {
        '.',  # 保留当前目录标识
        os.path.basename(backup_path),  # 提取'backup'
        # os.path.basename(error_path),       # 提取'error'
        # os.path.basename(week_path),        # 提取'WeekTask'
        os.path.basename(delete_path),  # 提取'delete_home'
        os.path.basename(old_path),  # 提取'old_folder'
    }

    def run(self):
        logger.set_file_logger(self.config.config_name)
        logger.hr('BackUp', 0)
        con = self.config.back_up.back_up_config
        # 检查并创建delete目录
        os.makedirs(delete_path, exist_ok=True)
        if con.backup_flag:
            # 根据文件创建时间移动旧文件到动态备份目录
            self.move_log_to_backup(log_path, backup_path, 1)
            # backup目录下，超过7天文件移动保存
            self.move_backup_to_old(backup_path, old_path, 7)
            # 每周一备份WeekTask文件夹
            self.move_week_to_backup(week_path, backup_path)

            # 删除指定目录中超过指定天数的文件，并清理空目录
            self.delete_old_files(delete_path, 7)
            self.delete_old_files(old_path, 30)
            # 递归删除空文件夹
            self.remove_empty_folders(log_path)

        con.backup_date = str(datetime.now().date())
        self.config.save()
        # self.push_notify(title='日志备份', content=f'今日备份完成!')
        self.set_next_run('BackUp', success=True, finish=True)
        raise TaskEnd

    def move_log_to_backup(self, base_path: str = log_path, back_dir: str = backup_path, days_threshold: int = 1):
        logger.hr(f'开始备份目录：[{base_path}]->[{back_dir}], 保留最近[{days_threshold}]天文件')

        # 递归遍历目录
        for root, dirs, files in os.walk(base_path):
            # 忽略隐藏文件和目录
            dirs[:] = [d for d in dirs
                       if not d.startswith('.')
                       and os.path.join(root, d) != back_dir
                       and os.path.join(root, d) != week_path]
            files = [f for f in files if not f.startswith('.')]

            for file_name in files:
                if file_name.split('.')[0] in log_names or file_name == 'server.log':
                    logger.warning(f'Skip [{file_name}]')
                    continue
                file_path = os.path.join(root, file_name)
                try:
                    file_stat = os.stat(file_path)
                    # 获取文件创建时间（跨平台兼容）
                    file_time = datetime.fromtimestamp(file_stat.st_ctime)
                    # 获取文件修改时间（跨平台兼容）
                    # file_time = datetime.fromtimestamp(file_stat.st_mtime)

                    # 计算时间差
                    today = datetime.now().date()
                    time_diff = (today - file_time.date()).days

                    if time_diff >= days_threshold:
                        # 构建动态备份路径（按年-月-日组织）
                        locale.setlocale(locale.LC_TIME, 'chinese')
                        date = file_time.strftime('%Y-%m-%d %A')
                        relative_path = os.path.relpath(root, base_path)  # 保留相对路径
                        backup_root = os.path.join(back_dir, date, relative_path)
                        # 检查并创建备份目录
                        os.makedirs(backup_root, exist_ok=True)

                        backup_file_path = os.path.join(backup_root, file_name)
                        shutil.move(file_path, backup_file_path)
                        logger.info(f'Move [{file_name}] ({time_diff} days ago) to [{backup_root}]')
                except Exception as e:
                    logger.error(f"Error processing [{file_name}]: {str(e)}")
        logger.hr(f'备份目录：[{base_path}]->[{back_dir}]完成!')

    def move_backup_to_old(self, base_dir: str = backup_path, old_dir: str = old_path, days_threshold: int = 7):
        logger.hr(f'开始备份目录：[{base_dir}]->[{old_dir}], 保留最近[{days_threshold}]天文件')
        try:
            # 验证源目录存在
            if not os.path.exists(base_dir):
                logger.error(f"❌ 错误：源目录不存在 {base_dir}")
                return
            if not os.path.isdir(base_dir):
                logger.error(f"❌ 错误：路径不是目录 {base_dir}")
                return

            # 准备完整目标路径
            os.makedirs(old_dir, exist_ok=True)
            logger.info(f"✅ 目标目录准备就绪：{old_dir}")

            current_date = datetime.now()
            # current_date = datetime(2025, 2, 19)  # 测试用日期

            for item in os.listdir(base_dir):
                item_path = os.path.join(base_dir, item)
                try:
                    # 跳过排除项
                    if not os.path.isdir(item_path):
                        logger.warning(f"⏩ 跳过非目录：{item}")
                        continue

                    if item in self.exclude_dirs:
                        logger.warning(f"⏩ 跳过排除目录：{item}")
                        continue

                    # 日期解析
                    match = re.search(r'\d{4}-\d{2}-\d{2}', item)
                    if not match:
                        logger.warning(f"⏩ 跳过无日期目录：{item}")
                        continue

                    try:
                        dir_date = datetime.strptime(match.group(), '%Y-%m-%d')
                    except ValueError as ve:
                        logger.warning(f"⚠️ 无效日期格式：{item} ({str(ve)})")
                        continue

                    # 计算日期差
                    delta = current_date - dir_date
                    if delta.days <= days_threshold:
                        logger.warning(f"⏩ 未过期目录：{item} ({delta.days}天)")
                        continue

                    # 移动操作
                    dest = os.path.join(old_dir, item)

                    try:
                        logger.info(f"🚚 正在移动：{item} -> {dest}")
                        shutil.move(item_path, dest)
                        logger.info(f"✅ 移动成功：{item}")
                    except FileNotFoundError:
                        logger.error(f"❌ 源目录不存在：{item}")
                    except PermissionError:
                        logger.error(f"❌ 权限不足：{item}")
                    except FileExistsError:
                        logger.error(f"❌ 目标已存在：{item}")
                    except Exception as e:
                        logger.error(f"❌ 移动失败：{item} ({str(e)})")

                except Exception as e:
                    logger.error(f"‼️ 处理目录异常：{item} ({str(e)})")
                    continue

        except Exception as e:
            logger.error(f"‼️ 全局异常：{str(e)}")
        logger.hr(f'备份目录：[{base_dir}]->[{old_dir}]完成!')

    def move_week_to_backup(self, base_dir: str = week_path, backup_dir: str = backup_path):
        logger.hr(f'开始备份目录：[{base_dir}]->[{backup_dir}]')

        # 检查当前日期是否为周一
        if datetime.now().weekday() != 0:  # 0 表示周一
            logger.info("今天不是周一，跳过移动操作")
            return

        # 获取源目录的文件夹名
        base_name = os.path.basename(base_dir)
        if not base_name:
            logger.error(f"❌ 错误：无法获取源目录名 {base_dir}")
            return

        # 构建目标路径
        target_date = datetime.now().strftime('%Y-%m-%d')
        target_name = f"{target_date} {base_name}"
        target_path = os.path.join(backup_dir, target_name)

        # 检查源目录是否存在
        if not os.path.exists(base_dir):
            logger.error(f"❌ 错误：源目录不存在 {base_dir}")
            return
        if not os.path.isdir(base_dir):
            logger.error(f"❌ 错误：路径不是目录 {base_dir}")
            return

        # 检查目标路径是否存在
        if os.path.exists(target_path):
            logger.error(f"❌ 错误：目标路径已存在 {target_path}")
            return

        # 移动操作
        try:
            logger.info(f"🚚 正在移动：{base_dir} -> {target_path}")
            shutil.move(base_dir, target_path)
            logger.info(f"✅ 移动成功：{base_dir} -> {target_path}")
        except FileNotFoundError:
            logger.error(f"❌ 源目录不存在：{base_dir}")
        except PermissionError:
            logger.error(f"❌ 权限不足：{base_dir}")
        except FileExistsError:
            logger.error(f"❌ 目标已存在：{target_path}")
        except Exception as e:
            logger.error(f"❌ 移动失败：{base_dir} -> {target_path} ({str(e)})")
        logger.hr(f'备份目录：[{base_dir}]->[{backup_dir}]完成!')

    def delete_old_files(self, base_path: str, days_threshold: int = 7):
        """删除指定目录中超过指定天数的文件，并清理空目录"""
        logger.hr(f"开始清理目录：[{base_path}], 保留最近[{days_threshold}]天的文件")

        # 计算时间差
        today = datetime.now().date()
        # 确保目录存在
        if not os.path.exists(base_path):
            logger.warning(f"目录不存在：{base_path}")
            return
        for root, dirs, files in os.walk(base_path, topdown=False):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    # 获取文件的修改时间
                    mtime = os.path.getmtime(file_path)
                    file_time = datetime.fromtimestamp(mtime)
                    time_diff = (today - file_time.date()).days
                    if time_diff >= days_threshold:
                        os.remove(file_path)
                        logger.info(f"删除文件：{file_path}（{time_diff}天前）")
                except Exception as e:
                    logger.error(f"删除文件失败：{file_path}，错误：{e}")
        logger.hr(f"清理目录：[{base_path}]完成!")

    def remove_empty_folders(self, path: str = log_path):
        """
        递归删除空文件夹
        :param path: 要检查的路径
        """
        logger.hr(f'开始删除空目录：[{path}]')
        abs_path = os.path.abspath(path)

        for root, dirs, files in os.walk(path, topdown=False):
            for dir_name in dirs:
                if dir_name in self.exclude_dirs:
                    logger.warning(f"⏩ 跳过排除目录：{dir_name}")
                    continue

                dir_path = os.path.join(root, dir_name)
                try:
                    # 排除符号链接目录和根目录
                    is_symbolic_link = os.path.islink(dir_path)
                    is_root_dir = os.path.samefile(dir_path, abs_path)
                    is_empty = not os.listdir(dir_path)
                except Exception as e:
                    logger.error(f"检查目录 {dir_path} 时发生意外错误: {e}")
                    continue

                if not is_symbolic_link and not is_root_dir and is_empty:
                    try:
                        os.rmdir(dir_path)
                        logger.info(f"Removed empty folder: {dir_path}")
                    except Exception as e:
                        logger.warning(f"Failed to remove {dir_path}: {str(e)}")
        logger.hr(f'删除空目录：[{path}]完成!')

    def get_real_path(self, path: str = log_path):
        """
        获取给定路径的真实路径，并检查目录是否存在。

        :param path: 相对于当前工作目录的路径
        :return: 真实路径，如果目录不存在则返回 None
        """
        try:
            # 获取当前工作目录
            current_directory = os.getcwd()

            # 构建 base_path 的完整路径
            full_path = os.path.join(current_directory, path)

            # 获取 base_path 的真实路径
            real_path = os.path.realpath(full_path)

            # 检查目录是否存在
            if os.path.exists(real_path) and os.path.isdir(real_path):
                # logger.info(f"真实目录路径: {real_path}")
                return real_path
            else:
                logger.info(f"目录 {real_path} 不存在")
                return None
        except Exception as e:
            logger.error(f"获取真实路径时发生错误: {e}")
            return None


if __name__ == '__main__':
    from module.config.config import Config
    from module.device.device import Device

    c = Config('du')
    d = Device(c)
    t = ScriptTask(c, d)

    t.run()
# if __name__ == "__main__":
# delete_old_files("./log/backup/delete_home",1)
