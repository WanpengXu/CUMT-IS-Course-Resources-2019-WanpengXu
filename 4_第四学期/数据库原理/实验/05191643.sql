-- 1
SELECT 姓名,课程名,成绩
FROM 学习,学生,课程,教师
WHERE 学习.学号=学生.学号 AND
	  学习.课程号=课程.课程号 AND
	  学习.教师号=教师.教师号 AND
	  教师名='王刚' AND
	  成绩>90;
        
-- 2
SELECT 姓名,学院名称
FROM 学生,学院
WHERE 学生.学院代码=学院.学院代码 AND
	  学号 IN(
		SELECT 学号
		FROM 学习
		WHERE 教师号 IN(
			SELECT 教师号
			FROM 教师
			WHERE 教师名='王刚'
			)
		);
            
-- 3
SELECT DISTINCT 学生.学号,姓名
FROM 学习,学生
WHERE 学习.学号=学生.学号 AND
	  学习.学号 NOT IN(
		SELECT 学习.学号
        FROM 学习
        WHERE 课程号 IN(
			SELECT 课程号
            FROM 课程
            WHERE 课程名='软件工程'
            )
        );

SELECT 学号,姓名
FROM 学生
WHERE 学号 NOT IN(
	SELECT 学号
    FROM 学习
    WHERE 课程号 IN(
		SELECT 课程号
        FROM 课程
        WHERE 课程名='软件工程'
        )
	);

-- 4
SELECT 学号
FROM 学习
GROUP BY 学号
HAVING COUNT(学号)>=2;

-- 5
SELECT 姓名,成绩
FROM 学习,学生
WHERE 学习.学号=学生.学号 AND
	  学习.学号 IN(
		SELECT 学号
		FROM 学习
		WHERE 课程号 IN(
			SELECT 课程号
			FROM 课程
			WHERE 课程名='经济学'
			)
		) AND
	  成绩<60;

-- 6
/*
SELECT 学号
FROM 学生
WHERE NOT EXISTS(
	(
	SELECT 课程号
    FROM 学习 AS First
    WHERE First.学号='T06'
    )
    EXCEPT
    (
	SELECT 课程号
	FROM 学习 AS Second
	WHERE Second.学号=学生.学号
    )
    ); 
    #mysql只支持UNION运算
*/

SELECT 学号
FROM 学生
WHERE NOT EXISTS(
	SELECT *
    FROM 学习 AS First
	WHERE First.学号='T06' AND
		  NOT EXISTS(
			SELECT *
			FROM 学习 AS Second
			WHERE Second.学号=学生.学号 AND
				  Second.课程号=First.课程号
			)
	);
    
#7
SELECT 姓名,学院名称
FROM 学生,学院
WHERE 学生.学院代码=学院.学院代码 AND
	  NOT EXISTS(
      SELECT *
      FROM 学习 AS First
      WHERE 课程号 IN ('C3','C4') AND
			NOT EXISTS(
            SELECT *
            FROM 学习 AS Second
            WHERE Second.学号=学生.学号 AND
				  First.课程号=Second.课程号
            )
      );
      
#8
SELECT 课程号,课程名
FROM 课程
WHERE 课程号 NOT IN(
	SELECT 课程号
    FROM 学习
    WHERE 学号 IN(
		SELECT 学号
        FROM 学生
        WHERE 姓名='王石'
        )
    );
    
#9
SELECT DISTINCT 课程.课程号
FROM 课程 LEFT OUTER JOIN 学习 ON 课程.课程号=学习.课程号
WHERE 学习.课程号 IS NULL;#学习.课程号其实没有消失

SELECT 课程号
FROM 课程
WHERE NOT EXISTS(#不存在要全false才能返回true
	SELECT *
    FROM 学习
    WHERE 课程.课程号=学习.课程号
    );
    
#10
SELECT 姓名
FROM 学生
WHERE NOT EXISTS(
	SELECT *
    FROM 课程
    WHERE NOT EXISTS(
		SELECT *
        FROM 学习
        WHERE 学生.学号=学习.学号 AND
			  课程.课程号=学习.课程号
        )
	);
-- 原数据无法验证正确性，增加一行后可验证
-- INSERT
-- INTO 学习
-- VALUES('T16','C7','5',88);

#11
SELECT 学院名称,AVG(成绩) AS 平均分
FROM 学习,学生,学院
WHERE 学习.学号=学生.学号 AND
	  学生.学院代码=学院.学院代码 AND
	  课程号 IN (
		SELECT 课程号
		FROM 课程
		WHERE 课程名='经济学'
		)
GROUP BY 学院名称;

#12
SELECT DISTINCT 姓名,学院名称,成绩
FROM 学生,学院,学习
WHERE 学生.学院代码=学院.学院代码 AND
	  学生.学号=学习.学号 AND
      学习.课程号 IN(
		SELECT 课程号
		FROM 课程
		WHERE 课程名='经济学'
		)
ORDER BY 学院名称,成绩 DESC;

#13
SELECT 课程.课程号,课程名,教师名
FROM 授课
	INNER JOIN 课程 ON 授课.课程号=课程.课程号
    INNER JOIN 教师 ON 授课.教师号=教师.教师号
WHERE 学时 BETWEEN 30 AND 45;

#14
SELECT 姓名
FROM 学习
	JOIN 学生 ON 学习.学号=学生.学号
    JOIN 课程 ON 学习.课程号=课程.课程号
WHERE 课程名='经济学'
ORDER BY 成绩 DESC
LIMIT 0,1;-- LIMIT 1 OFFSET 0;

#15
SELECT 课程.课程号,课程名
FROM 学习
	INNER JOIN 课程 ON 学习.课程号=课程.课程号
GROUP BY 学习.课程号
HAVING COUNT(*)>5;