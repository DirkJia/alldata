package com.platform.pc.front.controller;

import com.platform.pc.common.jedis.JedisClient;
import com.platform.pc.manager.dto.front.CommonDto;
import com.platform.pc.manager.dto.front.MemberLoginRegist;
import com.platform.pc.common.pojo.Result;
import com.platform.pc.common.utils.ResultUtil;
import com.platform.pc.manager.dto.front.Member;
import com.platform.pc.sso.service.LoginService;
import com.platform.pc.sso.service.MemberService;
import com.platform.pc.sso.service.RegisterService;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;

/**
 * @author wulinhao
 */
@RestController
@Api(description = "会员注册登录")
public class MemberController {

    private final static Logger log= LoggerFactory.getLogger(MemberController.class);

    @Autowired
    private LoginService loginService;
    @Autowired
    private RegisterService registerService;
    @Autowired
    private MemberService memberService;
    @Autowired
    private JedisClient jedisClient;

    @RequestMapping(value = "/member/login",method = RequestMethod.POST)
    @ApiOperation(value = "用户登录")
    public Result<Member> login(@RequestBody MemberLoginRegist memberLoginRegist,
                                HttpServletRequest request){
        Member member;
        member=loginService.userLogin(memberLoginRegist.getUserName(), memberLoginRegist.getUserPwd());
        // 验证失败
        if(member == null || (member != null && member.getState() == 0)){
            member.setMessage("验证失败");
        }
        return new ResultUtil<Member>().setData(member);
    }

    @RequestMapping(value = "/member/checkLogin",method = RequestMethod.GET)
    @ApiOperation(value = "判断用户是否登录")
    public Result<Member> checkLogin(@RequestParam(defaultValue = "") String token){

        Member member=loginService.getUserByToken(token);
        return new ResultUtil<Member>().setData(member);
    }

    @RequestMapping(value = "/member/loginOut",method = RequestMethod.GET)
    @ApiOperation(value = "退出登录")
    public Result<Object> logout(@RequestParam(defaultValue = "") String token){

        loginService.logout(token);
        return new ResultUtil<Object>().setData(null);
    }

    @RequestMapping(value = "/member/register",method = RequestMethod.POST)
    @ApiOperation(value = "用户注册")
    public Result<Object> register(@RequestBody MemberLoginRegist memberLoginRegist,
                                   HttpServletRequest request){
        // 注册
        int result=registerService.register(memberLoginRegist.getUserName(), memberLoginRegist.getUserPwd());
        if(result==0){
            return new ResultUtil<Object>().setErrorMsg("该用户名已被注册");
        }else if(result==-1){
            return new ResultUtil<Object>().setErrorMsg("用户名密码不能为空");
        }
        return new ResultUtil<Object>().setData(result);
    }

    @RequestMapping(value = "/member/imgaeUpload",method = RequestMethod.POST)
    @ApiOperation(value = "用户头像上传")
    public Result<Object> imgaeUpload(@RequestBody CommonDto common){

        String imgPath = memberService.imageUpload(common.getUserId(),common.getToken(),common.getImgData());
        return new ResultUtil<Object>().setData(imgPath);
    }
}