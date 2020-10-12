import logging
import os
import time

from src.unmerge_tools.unmerge import unmerge

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    filename = input('请输入excel文件名.后缀名: \n')
    if os.path.exists(filename):
        filename_unmerged = filename.replace('.xlsx', '_unmerged.xlsx')

        if not os.path.exists(filename_unmerged):
            logging.info("正在拆分合并单元格，请稍等……")
            new_workbook = unmerge(filename)
            new_workbook.save(filename.replace('.xlsx', '_unmerged.xlsx'))
            logging.info("拆分成功！新表写入到{}".format(filename_unmerged))
        else:
            logging.warning("{}已存在".format(filename_unmerged))
    else:
        logging.warning("文件" + filename + "不存在！")

    time.sleep(5)
