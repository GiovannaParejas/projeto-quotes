SELECT SYSDATE FROM DUAL;

CREATE TABLE quotes (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    quote_text VARCHAR2(1000) NOT NULL,
    author_name VARCHAR2(200) NOT NULL
);

INSERT INTO quotes (quote_text, author_name) VALUES ('Ser ou não ser', 'Shakespeare');
INSERT INTO quotes (quote_text, author_name) VALUES ('De tudo ao meu amor serei atento', 'Vinícius de Moraes');

COMMIT;
SELECT * FROM  quotes;

SELECT quote_text, author_name FROM quotes WHERE UPPER(author_name) LIKE '%SHAKE%';

