import React from 'react';
import { useState, useEffect } from 'react';
// import { ReactComponent as LogoSvg } from './img/logo.svg';
import './LoginForm.css';

function LoginForm() {

  return (
    <div className='login__wrapper'>
        <div className='login__blur'>
            <div className='login__ball'></div>
            <div className='login__ball'></div>
            <div className='login__ball'></div>
            <div className='login__ball'></div>
        </div>

        {/* <form action="" className='login__form loginform'>
            <h1 className='loginform__header'>Вход в «COGNI»</h1>
            <input type="text" placeholder='Введите логин' className='loginform__input'/>
            <input type="text" placeholder='Введите пароль' className='loginform__input'/>
            <button className='loginform__button'>Войти</button>
            <a href="" className='loginform__link'>Зарегистрироваться</a>
        </form> */}
        
        {/* <form action="" className='login__form loginform'>
            <h1 className='loginform__header'>Регистрация</h1>
            <input type="text" placeholder='Имя Фамилия' className='loginform__input'/>
            <input type="text" placeholder='Введите e-mail' className='loginform__input'/>
            <input type="text" placeholder='Придумайте пароль' className='loginform__input'/>
            <input type="text" placeholder='Подтвердите пароль' className='loginform__input'/>
            <label for="agreeRadio" className='loginform__label'><input type="radio" className='loginform__radio' id="agreeRadio"/><p>Согласен на обработку персональных данных <a href="" className='loginform__agree'>Пользовательское соглашение</a></p></label>
            <button className='loginform__button'>Продолжить</button>
            <p className='loginform__desc'>Уже есть аккаунт?</p>
            <a href="" className='loginform__link color-green'>Войти</a>
        </form> */}

        <form action="" className='login__form loginform'>
            <h1 className='loginform__header'>Введите свой тип <br/> личности</h1>
            <input type="text" placeholder='Ваш MBTI' className='loginform__input'/>
            <button className='loginform__button'>Зарегистрироваться</button>
            <p className='loginform__text'>или</p>
            <button className='loginform__button-other'>Пройти тест <br/> и узнать свой тип</button>
        </form>
       
        <div className='login__info info'>
            {/* <LogoSvg className='info__logo'/> */}
            <p className='info__logoText'>COGNI</p>
            <a href="" className='info__link'>О сервисе</a>
        </div>
    </div>
  );
};

export default LoginForm;
